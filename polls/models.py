from django.db import models

class Candidates(models.Model):
    objects = None
    name = models.TextField(max_length=30)
    counts = models.IntegerField()


