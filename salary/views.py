from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Salary
from .serializer import SalarySerializer
from rest_framework.views import APIView



class SalaryViewSet(ModelViewSet):
    
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    
    
