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
