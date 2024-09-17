from django.db import models
from personnel.models import Personnel


class Salary(models.Model):
    
    
    personnel = models.OneToOneField(Personnel, on_delete=models.CASCADE, related_name='sallaries', primary_key= True)

    base_salary = models.DecimalField(max_digits=10, decimal_places=3)
    housing_allowance = models.DecimalField(max_digits=10, decimal_places=3)
    child_allowance = models.DecimalField(max_digits=10, decimal_places=3)
    food_allowance= models.DecimalField(max_digits=10, decimal_places=3)
    salary_start_date = models.DateField()
    
   
    
    def __str__(self) :
        return f"{self.personnel.number_of_personnel} - {self.personnel.firstname}" 