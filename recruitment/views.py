from django.shortcuts import render
from .models import Recruitment
from .serializers import RecruitmentSerializer, RecruitmentDetailSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from core.views import BaseModelViewSet

"""
by viewset handle crud 
get all Recruiment data order by id:query
RecruitmentSerializer serialize the model of Recruiment 
"""


class RecruitmentViews(BaseModelViewSet):
    queryset = Recruitment.objects.order_by('recruiment_id').all()
    serializer_class = RecruitmentSerializer

    def get_queryset(self):
        recruitment_possition = self.kwargs.get("recruitment_possition")
        if recruitment_possition:
            queryset = Recruitment.objects.filter(
                recruitment_possition=recruitment_possition)
            if not queryset.exists():
                raise NotFound("Not found recruiment_possition!!!")
            return queryset

        return super().get_queryset()


class RecruitmentDetailViews(ModelViewSet):
    queryset = Recruitment.objects.order_by('recruiment_id').all()
    serializer_class = RecruitmentDetailSerializer

    def get_queryset(self):
        recruitment_condition = self.kwargs.get("recruitment_condition")
        if recruitment_condition:
            queryset = Recruitment.objects.filter(
                recruitment_condition=recruitment_condition)
            if not queryset.exists():
                raise NotFound("Not Found recruitment_condition!!!")
            return queryset

        return super().get_queryset()
