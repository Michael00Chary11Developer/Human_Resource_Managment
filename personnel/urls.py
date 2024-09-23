from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('manage', views.PersonnelViewSet, basename='personnel')

urlpatterns = [
    path('', include(router.urls)),
    path('position/<str:position>/',
         views.PersonnelViewSet.as_view({'get': 'list'})),
    path('level/<str:level_for_position>/',
         views.PersonnelViewSet.as_view({'get': 'list'})),
]
