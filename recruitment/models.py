from django.db import models
from datetime import datetime


class RecruitmentDateDetails(models.Model):
    id = models.AutoField(primary_key=True)
    recruitment_date = models.DateTimeField()
    numberـofـdaysـreceived = models.DateTimeField()
    numberـofـdaysـchecked = models.DateTimeField()
    numberـofـdays_confirmed = models.DateTimeField()
    

    def get_date_request(self):
        date_now = datetime.now()
        date_get = self.recruitment_date
        date_get_req = date_now-date_get

     


class RecruimentConditionDetails(models.Model):
    conditions_work = ["accepted", "reject", "uncertain"]
    position = ["Software Developer", "Front end Developer",
                "Full stack Developer", "App developer", "Web Developer"]
    recruiment_condition = models.CharField(
        max_length=15, choices=conditions_work, default="No Any Data")
    recruiment_position = models.CharField(
        max_length=50, choices=position, default="No Any Data")