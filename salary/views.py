from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Salary
from .serializer import SalarySerializer
from core.views import BaseModelViewSet


class SalaryViewSet(BaseModelViewSet):

    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
