from rest_framework import serializers
from .models import Salary
from personnel.models import Personnel
from .calculations import calculate_gross_salary, calculate_net_salary
from decimal import Decimal




class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['number_of_personnel','firstname', 'lastname']




class SalarySerializer(serializers.ModelSerializer):
    
    personnel = serializers.PrimaryKeyRelatedField(queryset=Personnel.objects.all(), write_only=True) 
    personnel_detail = PersonnelSerializer(source='personnel', read_only=True)

    gross_salary = serializers.SerializerMethodField(read_only=True)
    net_salary = serializers.SerializerMethodField(read_only=True)

    class Meta:
        
        
        model = Salary
        fields = ['user_id',
                  'personnel',
                  'personnel_detail',
                  'base_salary',
                  'housing_allowance',
                  'child_allowance',
                  'food_allowance',
                  'salary_start_date',
                  'gross_salary',
                  "net_salary",
                  'created_at',
                  'update_at'
                  ]
        
        read_only_fields = ['number_of_personnel', 'created_at', 'update_at', 'user_id']

        

    def get_gross_salary(self, obj: Salary) -> Decimal:
        return calculate_gross_salary(
            obj.base_salary, 
            obj.housing_allowance, 
            obj.child_allowance, 
            obj.food_allowance,
            obj.personnel.number_of_child,
            obj.personnel.marital_status.lower()
        )
    
    def get_net_salary(self, obj: Salary) -> Decimal:
        gross = self.get_gross_salary(obj)
        return calculate_net_salary(gross)
        
    def validate(self, data):
        # try:
        personnel=data.get('personnel')
        all_data_personnel=Personnel.objects.get(number_of_personnel=personnel)
        number_of_child=all_data_personnel.number_of_child
        child_allowance=data.get('child_allowance')
        # except Personnel.DoesNotExist:
        #     raise serializers.ValidationError(
        #         "Personnel with the given number does not exist.")

        if number_of_child is None or 0:
            if child_allowance is not None or not 0:
                raise serializers.ValidationError('single person or a married person that have not child cannot have child_allowance'
                                                  +'please enter it blank ir 0')


        if self.instance:
            if self.instance.personnel == personnel:
                return data

        if Salary.objects.filter(personnel=personnel).exists():
            raise serializers.ValidationError(f'A salary record for personnel {personnel} already exists.')

        return data
        