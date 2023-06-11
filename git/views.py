from rest_framework import viewsets
from .serializers import *
from .models import *

class CommitViewSet(viewsets.ModelViewSet):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer
