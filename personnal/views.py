from django.shortcuts import render
from .models import Personnal
from.serializer import PersonnalSerilizer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet



class CreatePersonnalView(ModelViewSet):
    queryset = Personnal.objects.all()
    serializer_class = PersonnalSerilizer

