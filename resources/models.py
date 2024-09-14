from .utils import CreateUniqueCode
from django.db import models


class Resources(models.Model):

    asset_code = models.CharField(
        max_length=8, editable=False, blank=False, primary_key=True)
    resource_name = models.CharField(
        max_length=20, blank=False, unique=False, editable=True)
    resource_sort = models.CharField(max_length=20, blank=True)
    dateـofـallocation = models.DateField()

    def save(self, *args, **kwargs):
        if not self.asset_code:
            self.asset_code = CreateUniqueCode.generate_unique_code(Resources)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.resource_name}\t{self.resource_sort}\t{self.dateـofـallocation}'
