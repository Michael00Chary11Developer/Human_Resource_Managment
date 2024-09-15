from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecruitmentViews

"""
router find Recruiment
router create automatically create urls 
use views for path
include -> the urls that router create
"""

router = DefaultRouter()
router.register("", RecruitmentViews, basename='RecruitmentRouter')

urlpatterns = [
    path('recruitment/', include(router.urls))
]
