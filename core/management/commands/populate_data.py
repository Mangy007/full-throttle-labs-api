import os
import json
import datetime

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError

from core.models import User, ActivityPeriod


class Command(BaseCommand):
    help = "Insert a .json file containing user details and their activity periods."

    def validate_date_format(self, date):
        date_format = "%b %d %Y %I:%M%p"
        try:
            datetime.datetime.strptime(date, date_format)
            return True
        except ValueError as e:
            return False

    def insert_to_db_and_get_user_details(self, data):
        try:
            user, is_created = User.objects.get_or_create(
                id=data["id"],
                real_name=data["real_name"],
                timezone=data["tz"]
            )
            return user
        except Exception as e:
            raise CommandError("Error in inserting {}: {}".format(
                User, str(e)))

    def insert_user_activity_to_db(self, user, data):
        try:
            if self.validate_date_format(data['start_time']) or self.validate_date_format(data['end_time']):
                ActivityPeriod.objects.create(
                    user=user,
                    start_time=data["start_time"],
                    end_time=data["end_time"]
                )
        except Exception as e:
            raise CommandError("Error in inserting {}: {}".format(
                ActivityPeriod, str(e)))

    def insert_user_details(self, data):
        user = self.insert_to_db_and_get_user_details(
            data)
        for activity in data['activity_periods']:
            self.insert_user_activity_to_db(user, activity)

    def get_current_app_path(self):
        return apps.get_app_config('core').path

    def get_json_file(self, filename):
        app_path = self.get_current_app_path()
        file_path = os.path.join(app_path, filename)
        return filename

    def add_arguments(self, parser):
        parser.add_argument('filenames',
                            nargs='+',
                            type=str,
                            help="Insert user activity records from json file")

    def handle(self, *args, **kwargs):
        for filename in kwargs['filenames']:
            file_path = self.get_json_file(filename)
            try:
                with open(file_path) as json_file:
                    data_list = json.load(json_file)
                    if isinstance(data_list, dict):
                        self.insert_user_details(data_list)
                    else:
                        for data in data_list:
                            self.insert_user_details(data)

            except FileNotFoundError:
                raise CommandError("File {} does not exist".format(
                    file_path))
