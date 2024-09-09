from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateAndGet

router = DefaultRouter()
router.register("", CreateAndGet)

urlpatterns = [
    path("recruitment/", include(router.urls))
]
