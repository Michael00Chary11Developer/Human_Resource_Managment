from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Salary
from .serializer import SalarySerializer
from core.views import BaseModelViewSet


class SalaryViewSet(BaseModelViewSet):

    """
    ViewSet for managing Salary records.

    This ViewSet provides the standard actions to create, read, update, 
    and delete Salary records for personnel.
    """

    queryset = Salary.objects.all()

    """
    The queryset that this view will operate on. 
    It retrieves all Salary records from the database.
    """
    serializer_class = SalarySerializer

    """
    The serializer class used to serialize and deserialize Salary data.
    """
