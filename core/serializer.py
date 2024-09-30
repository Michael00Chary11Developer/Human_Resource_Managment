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
        model = Resources
        fields = ['asset_code',
                  'resource_name',
                  'resource_sort',
                  'dateـofـallocation']


class SalaryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary
        fields = ['salary_start_date',
                  'gross_salary',
                  "net_salary",]


class PersonnelGetAllDataSerializer(serializers.ModelSerializer):

    salary_detail = SalaryDetailSerializer(read_only=True)
    resource_detail = SalaryDetailSerializer(read_only=True)

    class Meta:
        model = Personnel
        fields = ['number_of_personnel',
                  'firstname',
                  'lastname',
                  'position',
                  'resource_detail',
                  'salary_detail',
                  'date_of_employment',
                  'level_for_position',
                  ]
# [BaseCoreSerializer.Meta.fields[0]]+
# + [BaseCoreSerializer.Meta.fields[1] + BaseCoreSerializer.Meta.fields[2]]
