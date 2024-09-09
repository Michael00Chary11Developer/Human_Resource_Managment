from django.shortcuts import render
from .models import RecDate, RecCondition
from .serializers import ConditionSerializer, DateSerializer
from rest_framework.viewsets import ModelViewSet


class CreateAndGet(ModelViewSet):
    pass
