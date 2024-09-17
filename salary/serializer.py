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
    personnel = PersonnelSerializer()
    class Meta:
        
        
        model = Salary
        fields = ['personnel',
                #   'firstname',
                #   'lastname',
                  'base_salary',
                  'housing_allowance',
                  'child_allowance',
                  'food_allowance',
                  'salary_start_date',
                  ]
        
        
        def create(self, validated_data):
            personnel_data = validated_data.pop('personnel')
            
            personnel = Personnel.objects.get(number_of_personnel = personnel_data['number_of_personnel'])
            
            salary = Salary.objects.create(personnel=personnel, **validated_data)
            
            return salary
        
        
       
        # def update(self, instance, validated_data):
        #     personnel_data = validated_data.pop('personnel')
            
        #     personnel = Personnel.objects.get(number_of_personnel=personnel_data['number'])

    # def get_firstname(self, obj: Salary) -> str:

    #     return obj.personnel.firstname

    # def get_lastname(self, obj: Salary) -> str:

    #     return obj.personnel.lastname
