from rest_framework import serializers
from .models import Recruitment
from datetime import timedelta

"""
serialize model 
all filed except id 
id will be hid and not serialize
"""


class RecruitmentSerializer(serializers.ModelSerializer):

    time_spent = serializers.SerializerMethodField()

    class Meta:
        model = Recruitment
        fields = ['recieved_resume', 'checked_resume', 'approved_resume', 'interviewed_resume',
                  'duration_every_interview', 'recruitment_condition', 'date_recruitment',
                  'time_spent']
        

    def get_time_spent(self, obj: Recruitment) -> timedelta:
        return obj.interview_spent_time_calculate()

    def validate(self, data):
        recived_resume = data.get('recieved_resume')
        checked_resume = data.get("checked_resume")
        approved_resume = data.get('approved_resume')
        interviewed_resume = data.get('interviewed_resume')

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
