from django.urls import include, path
from rest_framework import routers
from .views import *
from .models import *

api_router = routers.DefaultRouter()
api_router.register(r'commits', CommitViewSet, basename='commits')

urlpatterns = [
    path('api/', include(api_router.urls)),
]
