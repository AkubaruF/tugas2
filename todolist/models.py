from django.db import models

# Create your models here.
class Task(models.Model):
    user = models.TextField()
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()