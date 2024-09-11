from django.urls import path, include
from. import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('manage', views.PersonnelViewSet, basename='personnel')

urlpatterns = [
    path('', include(router.urls)),
    path('position/<str:position>/', views.PersonnelViewSet.as_view({'get': 'list'})),
    
]
