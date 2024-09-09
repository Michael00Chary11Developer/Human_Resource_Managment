from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateAndGetCondition, CreateAndGetDate

router = DefaultRouter()
router.register("", CreateAndGetCondition)
router2 = DefaultRouter()
router2.register("", CreateAndGetDate)

urlpatterns = [
    path("condition/", include(router.urls)),
    path("date/", include(router2.urls)),

]
