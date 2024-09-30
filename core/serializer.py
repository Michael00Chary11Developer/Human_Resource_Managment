from rest_framework import serializers
from .models import BaseModelDate
from resources.models import Resources
from personnel.models import Personnel
from salary.models import Salary
from decimal import Decimal
from salary.utils import calculate_gross_salary, calculate_net_salary


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

    gross_salary = serializers.SerializerMethodField(read_only=True)

    """
    Computed gross salary for the personnel. This field is read-only.
    """
    net_salary = serializers.SerializerMethodField(read_only=True)

    """
    Computed net salary for the personnel after tax deductions. This field is read-only.
    """

    class Meta:
        model = Salary
        fields = ['salary_start_date',
                  'gross_salary',
                  "net_salary",]

    def get_gross_salary(self, obj: Salary) -> Decimal:
        """
        Calculate and return the gross salary for the personnel.

        The gross salary is calculated based on the base salary, housing allowance,
        child allowance, food allowance, number of children, and marital status of the personnel.
        """
        return calculate_gross_salary(
            obj.base_salary,
            obj.housing_allowance,
            obj.child_allowance,
            obj.food_allowance,
            obj.personnel.number_of_child,
            obj.personnel.marital_status.lower()
        )

    def get_net_salary(self, obj: Salary) -> Decimal:
        """
        Calculate and return the net salary for the personnel.

        The net salary is computed by deducting tax from the gross salary.
        """
        gross = self.get_gross_salary(obj)
        return calculate_net_salary(gross)


class PersonnelGetAllDataSerializer(serializers.ModelSerializer):

    salary_detail = serializers.SerializerMethodField()
    resource_detail = serializers.SerializerMethodField()

    class Meta:
        model = Personnel
        fields = [BaseCoreSerializer.Meta.fields[0]] + ['number_of_personnel',
                                                        'firstname',
                                                        'lastname',
                                                        'position',
                                                        'resource_detail',
                                                        'salary_detail',
                                                        'date_of_employment',
                                                        'level_for_position',
                                                        ] + [BaseCoreSerializer.Meta.fields[1]]+[BaseCoreSerializer.Meta.fields[2]]

    def get_salary_detail(self, obj: Personnel):
        salary = Salary.objects.filter(
            personnel=obj.number_of_personnel).first()
        if salary:
            return SalaryDetailSerializer(salary).data
        return None

    def get_resource_detail(self, obj: Personnel):
        resource = Resources.objects.filter(
            number_of_personnel=obj.number_of_personnel
        ).first()
        if Resources:
            return ResourcesDetailSerializer(resource).data
        return None
