from django.db import models
import pytz


class User(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    id = models.CharField(primary_key=True, max_length=10)
    real_name = models.CharField(max_length=100, null=False, blank=False)
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='UTC')

    def __str__(self):
        result = {
            'id': str(self.id),
            'real_name': str(self.real_name),
            'tz': str(self.timezone)
        }
        return str(result).replace("'", '"')


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.CharField(null=False, blank=False, max_length=50)
    end_time = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):

        result = {
            "start_time": str(self.start_time),
            "end_time": str(self.end_time)
        }
        return str(result).replace("'", '"')
