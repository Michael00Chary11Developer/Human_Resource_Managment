from django.shortcuts import render
from .models import Resources
from .serializers import ResourceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound


class ResourceView(ModelViewSet):
    """
    A viewset for viewing and editing Personnel instances.
    """
    """
    queryset= get all object Resource
    
    """
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer

    def get_queryset(self):
        personel_number = self.kwargs.get("number_of_personnel")
        if personel_number:
            queryset = Resources.objects.filter(
                number_of_personnel=personel_number)
            if not queryset.exists():
                raise NotFound("Not Found!!")
            return queryset

        resource_name = self.kwargs.get("resource_name")
        if resource_name is not None:
            queryset = Resources.objects.filter(
                resource_name=resource_name
            )
            if not queryset.exists():
                raise NotFound(f"{resource_name} is not found!")
            return queryset

        return super().get_queryset()
