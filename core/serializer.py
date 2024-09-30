from rest_framework import serializers
from .models import BaseModelDate


class BaseCoreSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    
    class Meta:
        model = BaseModelDate
        fields = ['user_id', 'created_at', 'update_at']
        read_only_fields = ['user_id', 'created_at', 'update_at']