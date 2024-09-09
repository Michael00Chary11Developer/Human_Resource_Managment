from rest_framework import serializers
from .models import RecruimentConditionDetails, RecruitmentDateDetails


class RecruimentConditionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruimentConditionDetails
        fields = ['daysـreceived', 'daysـchecked', 'days_confirmed',
                  'days_interviews', 'time_spent_interview']


class RecruitmentDateDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentDateDetails
        fields = ['__all__']
