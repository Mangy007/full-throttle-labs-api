from django.http import HttpResponse
from .models import User, ActivityPeriod
import json


def get_user_data_by_id(id):
    user = User.objects
    if len(user.filter(id=id)) > 0:
        return user.get(id=id)
    return None


def get_all_user_data():
    users = User.objects.all()
    if len(users) > 0:
        return users
    return None


def get_user_activity_details(user):
    activities_period = ActivityPeriod.objects.select_related().filter(user=user)
    activities = []
    if len(activities_period) > 0:
        activities = [activity.__str__() for activity in activities_period]
        return activities
    return activities


def get_by_id(response, id):
    user = get_user_data_by_id(id)
    user_details = {}
    if user is not None:
        user_details = json.loads(user.__str__())
        user_details["activity_periods"] = get_user_activity_details(
            user)
    return HttpResponse("<code>%s</code>" % str(user_details))


def get_all(response):
    users = get_all_user_data()

    users_dict = {
        "ok": False,
        "members": []
    }
    if users is not None:
        users_dict["ok"] = True
        for user in users:
            user_dict = json.loads(user.__str__())
            user_dict["activity_periods"] = get_user_activity_details(user)
            users_dict["members"].append(user_dict)
    return HttpResponse("<code>%s</code>" % str(users_dict))
