from rest_framework import serializers
from .models import  Personnel

class PersonnelSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = "__all__" 