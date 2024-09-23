from rest_framework import serializers
from .models import Recruitment
from datetime import timedelta

"""
Serializer for the Recruitment model.

This serializer handles the serialization and validation of
Recruitment instances. The id field is excluded from the
serialized output.

Attributes:
    time_spent (timedelta): A calculated field that represents the
                            total time spent on interviews.
"""


class RecruitmentSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Recruitment model.

    This class serializes all fields of the Recruitment model except
    for the `id` field, which is hidden and not included in the
    serialized output.

    Attributes:
        time_spent (SerializerMethodField): Calculates and returns
                                            the total time spent on
                                            interviews.
    """

    time_spent = serializers.SerializerMethodField()

    class Meta:
        model = Recruitment
        fields = ['user_id', 'recruiment_id', 'recieved_resume', 'checked_resume', 'approved_resume', 'interviewed_resume',
                  'duration_every_interview', 'recruitment_possition', "recruiment_level_possition", 'recruitment_condition', 'date_recruitment',
                  'created_at', 'update_at', 'time_spent']

        read_only_fields = ['user_id']

    def get_time_spent(self, obj: Recruitment) -> timedelta:
        """
        Calculate and return the total time spent on interviews.

        Args:
            obj (Recruitment): The instance of the Recruitment model.

        Returns:
            timedelta: The total time spent on interviews.
        """
        return obj.interview_spent_time_calculate()

    def validate(self, data):
        """
        Validate the dates related to the recruitment process to ensure
        logical consistency.

        The following conditions are checked:
        - The date when the resume was checked should not be after
          the date when it was received.
        - The date when the resume was approved should not be after
          the date when it was checked.
        - The date when the resume was interviewed should not be after
          the date when it was approved.

        Args:
            data (dict): A dictionary containing the data to validate.

        Returns:
            dict: The validated data.

        Raises:
            serializers.ValidationError: If any of the date conditions
                                          are not met.
        """
        recived_resume = data.get('recieved_resume')
        checked_resume = data.get("checked_resume")
        approved_resume = data.get('approved_resume')
        interviewed_resume = data.get('interviewed_resume')
        recruitment_condition = data.get('recruitment_condition')
        date_recruiment = data.get('date_recruitment')

        if recruitment_condition not in ["Accept", "accept"]:
            if date_recruiment is not None:
                raise serializers.ValidationError(
                    'No conditions other than being accepted can have an employment date. Please leave it blank')
        elif date_recruiment is None:
            raise serializers.ValidationError(
                'condition of Accept or accept must have date_recruiment')

        if recived_resume < checked_resume:
            raise serializers.ValidationError(
                'Checked resume date cannot be bigger than received resume date')

        if checked_resume < approved_resume:
            raise serializers.ValidationError(
                'Approved resume date cannot be bigger than received checked_resume')

        if approved_resume < interviewed_resume:
            raise serializers.ValidationError(
                'interviewed resume date cannot be bigger than received approved_resume')

        return data


class RecruitmentDetailSerializer(serializers.ModelSerializer):
    time_spent = serializers.SerializerMethodField()

    class Meta:
        model = Recruitment
        fields = ['duration_every_interview', 'recruitment_possition', 'recruitment_condition', 'date_recruitment',
                  'time_spent']

    def get_time_spent(self, obj: Recruitment) -> timedelta:
        """
        Calculate and return the total time spent on interviews.

        Args:
            obj (Recruitment): The instance of the Recruitment model.

        Returns:
            timedelta: The total time spent on interviews.
        """
        return obj.interview_spent_time_calculate()
