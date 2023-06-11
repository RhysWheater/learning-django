from django.db import models

class Commit(models.Model):
    repo = models.CharField(max_length=200)
    commit_id = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.repo}@{self.commit_id}"
