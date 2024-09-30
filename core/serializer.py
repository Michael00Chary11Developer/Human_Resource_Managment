from rest_framework import serializers
from .models import BaseModelDate
from resources.models import Resources
from personnel.models import Personnel
from salary.models import Salary


class BaseCoreSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = BaseModelDate
        fields = ['user_id', 'created_at', 'update_at']
        read_only_fields = ['user_id']


class ResourcesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        models = Resources
        fields = ['asset_code',
                  'resource_name',
                  'resource_sort',
                  'dateـofـallocation']


class SalaryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        models = Salary
        fields = ['salary_start_date',
                  'gross_salary',
                  "net_salary",]


class PersonnelGetAllData(serializers.ModelSerializer):

    salary_detail = SalaryDetailSerializer(read_only=True)
    resource_detail = SalaryDetailSerializer(read_only=True)

    class Meta:
        models = Personnel
        fields = BaseCoreSerializer.Meta.fields['user_id']
        +['number_of_personnel',
          'firstname',
          'lastname',
          'position',
          'level_for_position',
          'date_of_employment',
          ] + BaseCoreSerializer.Meta.fields['created_at'] + BaseCoreSerializer.Meta.fields['update_at']
