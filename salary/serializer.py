from rest_framework import serializers
from .models import Salary
from personnel.serializer import DynamicFieldsModelSerializer,PersonnelSerializer


class SalarySerializer(DynamicFieldsModelSerializer):

    personnel = PersonnelSerializer(fields=['number_of_personnel','firstname','lastname','degree'])

    class Meta:
        model = Salary
        fields = '__all__'