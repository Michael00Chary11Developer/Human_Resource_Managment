from rest_framework import serializers
from .models import Salary
from personnel.serializer import DynamicFieldsModelSerializer,PersonnelSerializer


class SalarySerializer(DynamicFieldsModelSerializer):

    # personnel = serializers.PrimaryKeyRelatedField(
    #     queryset=Personnel.objects.all())
    # firstname = serializers.SerializerMethodField()
    # lastname = serializers.SerializerMethodField()
    personnel = PersonnelSerializer(fields=['','firstname','lastname','degree'])

    class Meta:
        model = Salary
        # fields = ['personnel',
        #           'firstname',
        #           'lastname',
        #           'base_salary',
        #           'housing_allowance',
        #           'child_allowance',
        #           'food_allowance',
        #           'salary_start_date'
        #           ]
        fields = '__all__'

    # def get_firstname(self, obj: Salary) -> str:

    #     return obj.personnel.firstname

    # def get_lastname(self, obj: Salary) -> str:

    #     return obj.personnel.lastname
