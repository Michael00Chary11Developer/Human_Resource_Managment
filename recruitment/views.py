from django.shortcuts import render
from .models import Recruitment
from .serializers import RecruitmentSerializer
from rest_framework.viewsets import ModelViewSet

"""
by viewset handle crud 
get all Recruiment data order by id:query
RecruitmentSerializer serialize the model of Recruiment 
"""

class RecruitmentViews(ModelViewSet):
    queryset = Recruitment.objects.order_by('rec_id').all()
    serializer_class = RecruitmentSerializer