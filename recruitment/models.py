from django.db import models
from datetime import datetime


class RecruitmentDateDetails(models.Model):
    id = models.AutoField(primary_key=True)
    recruitment_date = models.DateField()
    numberـofـdaysـreceived = models.DurationField()
    numberـofـdaysـchecked = models.DurationField()
    numberـofـdays_confirmed = models.DurationField()
    numberـofـdays_interviews = models.DurationField()
    time_spent_interview = models.DurationField()


class RecruimentConditionDetails(models.Model):
    conditions_work = {"accepted": "Accepted",
                       "reject": "Reject", "uncertain": "Uncertain"}
    position = {"Software engineer": "software engineer", "Front end": "front end",
                "Full stack": "full stack", "App developer": "app developer", "Web developer": "web developer"}
    recruiment_condition = models.CharField(
        max_length=15, choices=conditions_work, default="No Any Data")
    recruiment_position = models.CharField(
        max_length=50, choices=position, default="No Any Data")
