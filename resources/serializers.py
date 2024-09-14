from .models import Resources
from rest_framework import serializers


class ResourceSerializer(serializers.ModelSerializer):
    code_of_asset = serializers.SerializerMethodField()

    class Meta:
        model = Resources
        fields = '__all__'