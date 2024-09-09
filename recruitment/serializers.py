from rest_framework import serializers
from .models import RecCondition, RecDate


class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecCondition
        fields = ['daysـreceived', 'daysـchecked', 'days_confirmed',
                  'days_interviews', 'time_spent_interview']


class DateSerializer(serializers.ModelSerializer):
    date_detail = ConditionSerializer

    class Meta:
        model = RecDate
        fields = ['__all__']
