from django.shortcuts import render
from .models import Personnel
from.serializer import PersonnelSerilizer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet



class CreatePersonnelView(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerilizer

