from django.db import models
from datetime import datetime


class RecCondition(models.Model):
    conditions_work = {"accepted": "Accepted",
                       "reject": "Reject", "uncertain": "Uncertain"}
    position = {"Software engineer": "software engineer", "Front end": "front end",
                "Full stack": "full stack", "App developer": "app developer", "Web developer": "web developer", "No information": "no information"}
    recruiment_condition = models.CharField(
        max_length=15, choices=conditions_work, default="uncertain")
    recruiment_position = models.CharField(
        max_length=50, choices=position, default="No information")


class RecDate(models.Model):
    id = models.AutoField(primary_key=True)
    recruitment_date = models.DateField()
    daysـreceived = models.DurationField()
    daysـchecked = models.DurationField()
    days_confirmed = models.DurationField()
    days_interviews = models.DurationField()
    time_spent_interview = models.DurationField()
    recruitment_details = models.OneToOneField(
        RecCondition, on_delete=models.CASCADE, related_name='date_detail')
