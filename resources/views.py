from django.shortcuts import render
from .models import Resources
from .serializers import ResourceSerializer
from rest_framework.viewsets import ModelViewSet


class ResourceView(ModelViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer