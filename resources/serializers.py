from .models import Resources
from rest_framework import serializers
from personnel.models import Personnel

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


class PersonnelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personnel
        fields = ['number_of_personnel', 'firstname', 'lastname']


class ResourceSerializer(serializers.ModelSerializer):

    number_of_personnel_ex = PersonnelSerializer(read_only=True)

    class Meta:
        model = Resources
        fields = ['user_id', 'personnel_number', 'number_of_personnel_ex',
                  'asset_code', 'resource_name', 'resource_sort', 'dateـofـallocation',
                  'created_at', 'update_at']
