from rest_framework import serializers
from .models import  Personnel
from datetime import datetime

class PersonnelSerializer(serializers.ModelSerializer):
    
    """
    Serializer for the Personnel model.

    This serializer handles the conversion between Personnel model instances
    and JSON representations, allowing for easy input and output of personnel
    data through API endpoints.
    """
    
    class Meta:
        model = Personnel
        fields = ['number_of_personnel'
                  ,'firstname', 
                  'lastname', 
                  'phone_number', 
                  'birth_date', 
                  'degree', 
                  'field_of_study', 
                  'career_records', 
                  'position', 
                  'level_for_position', 
                  'date_of_employment'
                  ] 
        
        """
        Include all fields from the Personnel model in the serialized output.
        """
        
    def validate(self, data):
        """
    Validate the input data for the PersonnelSerializer.

    This method checks the following conditions:
    1. Ensures that the 'birth_date' is not in the future.
    2. Ensures that the 'date_of_employment' is not before the 'birth_date'.

    Args:
        data (dict): The input data containing the fields to be validated.

    Raises:
        serializers.ValidationError: If the 'birth_date' is in the future or if the
        'date_of_employment' is before the 'birth_date'.

    Returns:
        dict: The validated data if no errors are raised.
    """
        
        birth_date = data.get('birth_date')
        date_of_employment = data.get("date_of_employment")
        today = datetime.now().date()
        
        if birth_date > today:
            raise serializers.ValidationError('Birth date cannot be in the future') 
        
        if date_of_employment < birth_date:
            raise serializers.ValidationError('Date of employment cannot be before birth date.')       
        
        return data
        
        