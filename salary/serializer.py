from rest_framework import serializers
from .models import Salary


class SalarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Salary
        fields = ['personnel', 
                  'base_salary', 
                  'housing_allowance', 
                  'child_allowance', 
                  'food_allowance', 
                  'salary_start_date'
                  ]