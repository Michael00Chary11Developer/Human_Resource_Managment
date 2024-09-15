from django.db import models
from personnel.models import Personnel


class Salary(models.Model):
    
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE, related_name='sallaries')

    base_salary = (models.DecimalField(max_digits=10, decimal_places=3))
    housing_allowance = (models.DecimalField(max_digits=10, decimal_places=2))
    child_allowance = (models.DecimalField(max_digits=10, decimal_places=2))
    food_allowance= (models.DecimalField(max_digits=10, decimal_places=2))
    salary_start_date = (models.DateField())
    
    def __str__(self) :
        return f"{self.personnel.number_of_personnel} - {self.personnel.firstname} - {self.base_salary}" 