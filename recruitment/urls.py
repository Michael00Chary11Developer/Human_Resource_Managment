from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecruitmentViews

router = DefaultRouter()
router.register("", RecruitmentViews, basename='RecruitmentRouter')

urlpatterns = [
    path('views/', include(router.urls))
]
