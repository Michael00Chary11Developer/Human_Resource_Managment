from django.shortcuts import render
from .models import RecDate, RecCondition
from .serializers import ConditionSerializer, DateSerializer
from rest_framework.viewsets import ModelViewSet


class CreateAndGetCondition(ModelViewSet):
    queryset = RecCondition.objects.order_by('id').all()
    serializer_class = ConditionSerializer


class CreateAndGetDate(ModelViewSet):
    queryset = RecDate.objects.order_by('id').all()
    serializer_class = DateSerializer
    http_method_names = ['get', 'put', 'patch', 'head', 'options', 'trace', 'delete',]

