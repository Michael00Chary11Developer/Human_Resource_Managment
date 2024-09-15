from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('manage', views.SalaryViewSet, basename='salary')

urlpatterns = [
    path('', include(router.urls)),
]
