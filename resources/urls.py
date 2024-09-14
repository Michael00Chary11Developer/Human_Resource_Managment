from django.urls import path, include
from .views import ResourceView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('resource', ResourceView)


urlpatterns = [
    path('', include(router.urls)),
]