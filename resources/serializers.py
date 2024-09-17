from .models import Resources
from rest_framework import serializers

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


class ResourceSerializer(serializers.ModelSerializer):

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = Resources
        fields = ['number_of_personnel', 'first_name',
                  'last_name', 'asset_code',
                  'resource_name', 'resource_sort',
                  'dateـofـallocation']

    def get_first_name(self, obj: Resources):
        first_name = obj.number_of_personnel.firstname
        return first_name

    def get_last_name(self, obj: Resources):
        last_name = obj.number_of_personnel.lastname
        return last_name
