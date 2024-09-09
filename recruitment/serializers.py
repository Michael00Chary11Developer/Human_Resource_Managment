from rest_framework import serializers
from .models import RecCondition, RecDate


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecDate
        fields = '__all__'

class ConditionSerializer(serializers.ModelSerializer):
    rec_date = DateSerializer(read_only=True)
    class Meta:
        model = RecCondition
        fields = '__all__'



