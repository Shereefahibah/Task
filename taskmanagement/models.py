from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    completed=models.BooleanField(default=False)
