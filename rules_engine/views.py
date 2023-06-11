from rest_framework import viewsets
from .serializers import *
from .models import *

class EngineViewSet(viewsets.ModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
