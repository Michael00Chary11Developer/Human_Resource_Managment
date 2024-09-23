from .models import Resources
from rest_framework import serializers
from personnel.models import Personnel
from django.utils import timezone

"""
serializr class that serialize mean convert json to python object python object to json
    Attributes:
        get all attribute of Resourcse in fields for serialize:
                asset_code (str): A unique identifier for the resource. This field is set automatically
                          if not provided, using a method from CreateUniqueCode.
                          CreateUniqueCode is in utils.py
                resource_sort (str): The category or type of the resource. This field is optional.
                date_of_allocation (date): The date when the resource was allocated. This field is required.
    models:
        Resource and say which model must be serialize         
"""


class PersonnelDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personnel
        fields = ['number_of_personnel',
                  'firstname',
                  'lastname']


class ResourceSerializer(serializers.ModelSerializer):

    personnel_detail = PersonnelDetailSerializer(
        source="personnel_number", read_only=True)

    class Meta:
        model = Resources
        fields = ['user_id',
                  'personnel_number',
                  'personnel_detail',
                  'asset_code',
                  'personnel_number',
                  'resource_name',
                  'resource_sort',
                  'dateـofـallocation',
                  'created_at',
                  'update_at']
        read_only_fields = ['user_id']

    def validate(self, data: Resources):
        today = timezone.now().date()
        date_time_allocation = data.get("dateـofـallocation")
        if date_time_allocation > today:
            raise serializers.ValidationError(
                "The data of aalocation cannot be in future!")
        return data
