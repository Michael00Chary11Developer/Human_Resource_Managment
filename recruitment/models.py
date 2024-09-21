from typing import Any, Iterable
from django.db import models
from datetime import timedelta
from core.models import BaseModelDate
from uuid import uuid4
"""
The usage model is defined, 
which includes a method for selecting interview times and 
some fields for the model
"""


class Recruitment(BaseModelDate):
    """_summary_
    ID is the primary key. It fills automatically
    condition_choices and possition_choices must be chosen in recruitment_condition and recruitment_possition
    """

    recruiment_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    """
    Fields:
        recruiment_id (AutoField): The primary key for the model, automatically filled.
        recruitment_possition (CharField): The position being recruited for
        recieved_resume (PositiveIntegerField): Number of resumes received.
        checked_resume (PositiveIntegerField): Number of resumes checked.
        approved_resume (PositiveIntegerField): Number of resumes approved.
        interviewed_resume (PositiveSmallIntegerField): Number of resumes that went through interviews.
        duration_every_interview (DurationField): Duration of each interview, stored as a timedelta object.
        recruitment_condition (CharField): The current condition of the recruitment
        date_recruitment (DateField): The date of the recruitment.

    Methods:
        __str__(): Returns a human-readable string representation of the recruitment instance.
        interview_spent_time_calculate(): Calculates the total time spent on interviews.
    """

    recieved_resume = models.PositiveIntegerField()
    checked_resume = models.PositiveIntegerField()
    approved_resume = models.PositiveIntegerField()
    interviewed_resume = models.PositiveSmallIntegerField()
    duration_every_interview = models.DurationField()
    recruitment_possition = models.CharField(
        max_length=50,  default='Nothing')
    recruiment_level_possition = models.CharField(
        max_length=50, default='Nothing'
    )
    recruitment_condition = models.CharField(
        max_length=50, default='Uncertain')
    date_recruitment = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the Person object.
        Readable for date_recruitment and recruitment_condition
        """
        return f"date recruiment:{self.date_recruitment}\tcondition:{self.recruitment_condition}"

    def interview_spent_time_calculate(self) -> timedelta:
        convertor_int = int(self.duration_every_interview.total_seconds())
        total_seconds = self.interviewed_resume*convertor_int
        return str(timedelta(seconds=total_seconds))
