from .models import Resources
from rest_framework import serializers


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'
        
