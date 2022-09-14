from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import datetime, date

class Person(models.Model):
    display_name = models.CharField(max_length = 30)
    display_npm = models.CharField(max_length = 10)

class Post(models.Model):
    author = models.ForeignKey(Person, on_delete = models.CASCADE)
    content = models.CharField(max_length = 125)
    published_date = models.DateTimeField(default = timezone.now)