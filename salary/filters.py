from salary.models import Salary
import django_filters

class CustomSalaryFilter(django_filters.FilterSet):
    class Meta:
        model = Salary
        fields=(
            'base_salary',
        )      