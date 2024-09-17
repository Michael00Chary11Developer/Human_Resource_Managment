from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Salary
from .serializer import SalarySerializer
from salary.filters import CustomSalaryFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class SalaryViewSet(ModelViewSet):
    
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    # filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    # # filter_backends=[CustomSalaryFilter,]
    # search_fields=['base_salary']
    # filterset_fields=['base_salary']