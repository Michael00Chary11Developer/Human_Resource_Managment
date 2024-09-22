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

    personnel = serializers.PrimaryKeyRelatedField(queryset=Personnel.objects.all(), write_only=True) 
    personnel_detail = PersonnelSerializer(
        read_only=True, source='personnel_number')

    class Meta:
        model = Resources
        fields = ['user_id','personnel' ,'personnel_number', 'personnel_detail',
                  'asset_code', 'resource_name', 'resource_sort', 'dateـofـallocation',
                  'created_at', 'update_at']

    def validate(self, data):
        personnel = data.get('personnel')

        if self.instance:
            if self.instance.personnel == personnel:
                return data

        if Resources.objects.filter(personnel=personnel).exists():
            raise serializers.ValidationError(f'A Resource record for personnel {personnel} already exists.')

        return data