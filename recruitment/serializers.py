from rest_framework import serializers
from .models import Recruitment

"""
serialize model 
all filed except id
"""


class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'
