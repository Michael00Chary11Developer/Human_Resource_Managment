from rest_framework.exceptions import NotFound
from .models import Personnel
from .serializer import PersonnelSerializer
from core.views import BaseModelViewSet
from .serializer import PersonnelGetAllDetailSerializer


class PersonnelViewSet(BaseModelViewSet):

    """
    A viewset for viewing and editing Personnel instances.

    This viewset provides CRUD operations for personnel records and includes filtering
    options based on personnel's position and level.
    """
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

    def get_queryset(self):
        """
        Optionally filter the returned personnel instances based on
        the 'position' and 'level_for_position' parameters.

        Returns:
            queryset: A filtered queryset of Personnel instances.

        Raises:
            NotFound: If no personnel are found with the specified position or level.
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


class PersonnelGetAllViewSet(BaseModelViewSet):
    queryset = Personnel.objects.order_by('created_at').all()
    serializer_class = PersonnelGetAllDetailSerializer
