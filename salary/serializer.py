from rest_framework import serializers
from .models import Salary
from personnel.models import Personnel






class SalarySerializer(serializers.ModelSerializer):
    
    personnel = serializers.PrimaryKeyRelatedField(queryset=Personnel.objects.all())
    firstname = serializers.SerializerMethodField()
    lastname = serializers.SerializerMethodField()
    
    class Meta:
        model = Salary
        fields = ['personnel',
                  'firstname',
                  'lastname', 
                  'base_salary', 
                  'housing_allowance', 
                  'child_allowance', 
                  'food_allowance', 
                  'salary_start_date'
                  ]
        
        
        
    def get_firstname(self, obj):
        
        return obj.personnel.firstname
    
    def get_lastname(self, obj):
        
        return obj.personnel.lastname
  
        


 