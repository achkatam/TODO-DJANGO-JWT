from django.db import models
from datetime import datetime


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=500, null=False)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return self.name
