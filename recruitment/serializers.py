from rest_framework import serializers
from .models import Recruitment

"""
serialize model 
all filed except id 
id will be hid and not serialize
"""


class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = ['recieved_resume','checked_resume','approved_resume','interviewed_resume',
                  'time_spent_every_interview','recruitment_condition','date_recruitment']
