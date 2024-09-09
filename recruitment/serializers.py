from rest_framework import serializers
from .models import RecCondition, RecDate


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecDate
        fields = ["recruitment_date", "daysـreceived", "daysـchecked",
                  "days_confirmed", "days_interviews", "time_spent_interview"]


class ConditionSerializer(serializers.ModelSerializer):
    rec_date = DateSerializer(read_only=True)

    class Meta:
        model = RecCondition
        fields = ['rec_date', 'recruiment_condition', "recruiment_position"]
