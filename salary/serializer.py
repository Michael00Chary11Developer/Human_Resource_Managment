from rest_framework import serializers
from .models import Salary
from personnel.models import Personnel


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['number_of_personnel','firstname', 'lastname']




class SalarySerializer(serializers.ModelSerializer):
    
    # firstname = serializers.SerializerMethodField()
    # lastname = serializers.SerializerMethodField()
    personnel = serializers.PrimaryKeyRelatedField(queryset=Personnel.objects.all(), write_only=True) 
    personnel_detail = PersonnelSerializer(source='personnel', read_only=True)
    class Meta:
        
        
        model = Salary
        fields = ['personnel',
                  'personnel_detail',
                #   'firstname',
                #   'lastname',
                  'base_salary',
                  'housing_allowance',
                  'child_allowance',
                  'food_allowance',
                  'salary_start_date',
                  ]
        
    def validate(self, data):
        personnel = data.get('personnel')

        if Salary.objects.filter(personnel=personnel).exists():
            raise serializers.ValidationError(f'A salary record for personnel {personnel} already exists.')
        
        return data
        
        
        

    # def get_firstname(self, obj: Salary) -> str:

    #     return obj.personnel.firstname

    # def get_lastname(self, obj: Salary) -> str:

    #     return obj.personnel.lastname
