from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=50)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=100)


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User,related_name="activityperiods",on_delete=models.PROTECT)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

