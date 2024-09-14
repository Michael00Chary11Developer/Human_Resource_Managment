from django.db import models
from random import randint


class Resources(models.Model):
    resource_name = models.CharField(
        max_length=20, blank=False, unique=False, editable=False)
    dateـofـallocation = models.DateField()
    asset_code = models.CharField(max_length=10)
