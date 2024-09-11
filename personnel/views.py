from django.shortcuts import render
from .models import Personnel
from.serializer import PersonnelSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound



class PersonnelViewSet(ModelViewSet):
    
    """
    A viewset for viewing and editing Personnel instances.
    """
    
    serializer_class = PersonnelSerializer
    
    
    def get_object(self):
        personnel_number = self.kwargs.get('pk')
        return Personnel.objects.get(number_of_personnel=personnel_number)
    
    def get_queryset(self):
        queryset = Personnel.objects.all()
        position = self.kwargs.get('position')
        
        queryset = Personnel.objects.filter(position=position)
        return queryset
            
    
    
    
