from django.db import models
from git.models import Commit

class Engine(models.Model):
    version = models.CharField(max_length=200)
    commit = models.ForeignKey(Commit, on_delete=models.CASCADE, related_name='engine_commit')
    created = models.DateTimeField(auto_now_add=True)
