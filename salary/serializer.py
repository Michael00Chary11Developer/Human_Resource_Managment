from rest_framework import serializers
from .models import Salary
from personnel.models import Personnel
from .calculations import calculate_gross_salary, calculate_net_salary
from decimal import Decimal




class PersonnelSerializer(serializers.ModelSerializer):

    """
    Serializer for the Personnel model.

    This serializer converts the Personnel model fields into JSON format.
    """
    class Meta:
        model = Personnel
        fields = ['number_of_personnel','firstname', 'lastname']




class SalarySerializer(serializers.ModelSerializer):

    """
    Serializer for the Salary model.

    This serializer handles the serialization and validation of salary data
    for personnel, including the calculation of gross and net salaries.
    """
    
    personnel = serializers.PrimaryKeyRelatedField(queryset=Personnel.objects.all(), write_only=True) 

    """
    The personnel associated with the salary. This field is write-only.
    """
    personnel_detail = PersonnelSerializer(source='personnel', read_only=True)

    """
    Detailed information about the personnel. This field is read-only.
    """

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

        """
        List of fields that cannot be modified during serialization.
        """

        

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
        
    def validate(self, data):

        """
        Validate the salary data before saving.

        This method checks whether the personnel is eligible for child allowance
        based on their marital status and number of children. It also ensures that
        there is no existing salary record for the same personnel.
        """
        personnel:Personnel=data.get('personnel')
        child_allowance=data.get('child_allowance')
        salary_start_date=data.get('salary_start_date')
        
        if salary_start_date < personnel.date_of_employment:
            raise serializers.ValidationError("The salary_start_date cannot being ahead of date_of_employment")

        if personnel.marital_status == 'single' or (personnel.marital_status == 'married' and personnel.number_of_child in [0, None]):

            if child_allowance not in [0, None]:

                raise serializers.ValidationError("Personnel with no children or single cannot have a child allowance.")
            

        if self.instance:
            if self.instance.personnel == personnel:
                return data

        if Salary.objects.filter(personnel=personnel).exists():
            raise serializers.ValidationError(f'A salary record for personnel {personnel} already exists.')

        return data
        