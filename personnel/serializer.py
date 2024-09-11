from rest_framework import serializers
from .models import  Personnel

class PersonnelSerializer(serializers.ModelSerializer):
    
    """
    Serializer for the Personnel model.

    This serializer handles the conversion between Personnel model instances
    and JSON representations, allowing for easy input and output of personnel
    data through API endpoints.
    """
    
    class Meta:
        model = Personnel
        fields = "__all__" 
        
        """
        Include all fields from the Personnel model in the serialized output.
        """
        