from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from rest_framework import viewsets
from .serializers import *
from .models import *

class EngineViewSet(viewsets.ModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer

class EngineListView(ListView):
    model = Engine
    template_name = 'engines.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Engine.objects.all()
