from django.shortcuts import render
from .models import Personnel
from.serializer import PersonnelSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet



class PersonnelViewSet(ModelViewSet):
    
    """
    A viewset for viewing and editing Personnel instances.
    """
    
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    
    
    def get_object(self):
        personnel_number = self.kwargs.get('pk')
        return Personnel.objects.get(number_of_personnel=personnel_number)
