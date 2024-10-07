from .models import Recruitment
from .serializers import RecruitmentSerializer, RecruitmentDetailSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from core.views import BaseModelViewSet


"""
RecruitmentViews and RecruitmentDetailViews handle CRUD operations and filtering of Recruitment data.

- RecruitmentViews: Handles general recruitment data.
    - Orders recruitment data by 'recruiment_id'.
    - Filters by 'recruitment_possition' if provided in the URL.

- RecruitmentDetailViews: Handles detailed recruitment data.
    - Filters by 'recruitment_condition' if provided in the URL.

viewset manage data by crud,get,put,push,get,get by pk,delete,patch
"""


class RecruitmentViews(BaseModelViewSet):
    """
    Viewset for managing general recruitment data.

    - Handles listing, creating, updating, and deleting Recruitment records.
    - Orders recruitment data by 'recruiment_id'.
    - If 'recruitment_possition' is provided in the URL, filters the queryset by that position.
    - Uses 'RecruitmentSerializer' to serialize the Recruitment model.
    """
    queryset = Recruitment.objects.order_by('date_recruitment').all()
    serializer_class = RecruitmentSerializer

    def get_queryset(self):
        """
        Overrides the default 'get_queryset' method to filter by 'recruitment_condition' if provided.
        """
        recruitment_possition = self.kwargs.get("recruitment_possition")
        if recruitment_possition:
            queryset = Recruitment.objects.filter(
                recruitment_possition=recruitment_possition)
            if not queryset.exists():
                raise NotFound("Not found recruiment_possition!!!")
            return queryset

        return super().get_queryset()


class RecruitmentDetailViews(ModelViewSet):
    """
    Viewset for managing detailed recruitment data.

    - Handles detailed retrieval of recruitment data based on 'recruitment_condition'.
    - Orders recruitment data by 'recruiment_id'.
    - Uses 'RecruitmentDetailSerializer' to serialize the detailed Recruitment model.
    """
    queryset = Recruitment.objects.order_by('date_recruitment').all()
    serializer_class = RecruitmentDetailSerializer

    def get_queryset(self):
        """
        Overrides the default 'get_queryset' method to filter by 'recruitment_condition' if provided.
        """
        recruitment_condition = self.kwargs.get("recruitment_condition")
        if recruitment_condition:
            queryset = Recruitment.objects.filter(
                recruitment_condition=recruitment_condition)
            if not queryset.exists():
                raise NotFound("Not Found recruitment_condition!!!")
            return queryset

        return super().get_queryset()
