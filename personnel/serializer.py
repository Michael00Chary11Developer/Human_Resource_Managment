from rest_framework import serializers
from .models import Personnel
from datetime import datetime



class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class PersonnelSerializer(DynamicFieldsModelSerializer):
    """
    Serializer for the Personnel model.

    This serializer handles the conversion between Personnel model instances
    and JSON representations, allowing for easy input and output of personnel
    data through API endpoints.
    """

    class Meta:
        model = Personnel
        fields = [
            'number_of_personnel',
            'firstname',
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
        read_only_fields = ['number_of_personnel']

        """
        Include all fields from the Personnel model in the serialized output.
        """

    def validate(self, data):
        """
        Validate the input data for the PersonnelSerializer.

        This method checks the following conditions:
        1. Ensures that the 'birth_date' is not in the future.
        2. Ensures that the 'date_of_employment' is not before the 'birth_date'.
        3. Ensures that the 'date_of_employment' is not in the future.

        Args:
            data (dict): The input data containing the fields to be validated.

        Raises:
            serializers.ValidationError: If any of the validation checks fail.

        Returns:
            dict: The validated data if no errors are raised.
        """

        birth_date = data.get('birth_date')
        date_of_employment = data.get('date_of_employment')
        today = datetime.now().date()

        if birth_date > today:
            raise serializers.ValidationError(
                'Birth date cannot be in the future.')

        if date_of_employment < birth_date:
            raise serializers.ValidationError(
                'Date of employment cannot be before birth date.')

        if date_of_employment > today:
            raise serializers.ValidationError(
                'Date of employment cannot be in the future.')

        return data
