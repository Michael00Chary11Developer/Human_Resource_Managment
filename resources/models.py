from django.db import models
from random import randint
from .utils import CreateUniqueCode


class Resources(models.Model):
    
    resource_name = models.CharField(
        max_length=20, blank=False, unique=False, editable=False)
    resource_sort=models.CharField(max_length=2,blank=True)
    dateـofـallocation = models.DateField()