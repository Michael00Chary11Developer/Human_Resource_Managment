from django.urls import path, include
from .views import ResourceView
from rest_framework.routers import DefaultRouter

"""
urls:
    method:
        DefaultRouter:
            method that set automatically urls for modelviewset
        register:
            register method to ResourceView
    optional:
        urlspattern we set router.urls that create by DefaultRouter
"""


router = DefaultRouter()
router.register('manage', ResourceView)


urlpatterns = [
    path('', include(router.urls)),
    path("personel/<int:number_of_personnel>",
         ResourceView.as_view({"get": "list"})),
    path('resource_name/<str:resource_name>',
         ResourceView.as_view({"get": "list"}))
]
