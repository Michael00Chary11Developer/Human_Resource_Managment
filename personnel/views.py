from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render
from .models import Personnel
from .serializer import PersonnelSerializer


class PersonnelViewSet(ModelViewSet):

    """
    A viewset for viewing and editing Personnel instances.
    """
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

    # def get_object(self):
    #     """
    #     Retrieve a personnel instance by its unique number.
    #     """
    #     personnel_number = self.kwargs.get('pk')
    #     try:
    #         return Personnel.objects.get(number_of_personnel=personnel_number)
    #     except Personnel.DoesNotExist:
    #         raise NotFound('Personnel not found')

    def get_queryset(self):
        """
        Optionally filter the returned personnel instances based on
        the 'position' and 'level_for_position' parameters.
        """

        position = self.kwargs.get('position')
        level_for_position = self.kwargs.get("level_for_position")
        if position:
            queryset = Personnel.objects.filter(position=position)
            if not queryset.exists():
                raise NotFound(f'No personnel found with position: {position}')
            return queryset

        if level_for_position:
            queryset = Personnel.objects.filter(
                level_for_position=level_for_position)
            if not queryset.exists():
                raise NotFound(f'No personnel found with level')
            return queryset

        return super().get_queryset()
