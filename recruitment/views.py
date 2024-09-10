from django.shortcuts import render
from .models import Recruitment
from .serializers import RecruitmentSerializer
from rest_framework.viewsets import ModelViewSet


class RecruitmentViews(ModelViewSet):
    queryset = Recruitment.objects.order_by('rec_id').all()
    serializer_class = RecruitmentSerializer
