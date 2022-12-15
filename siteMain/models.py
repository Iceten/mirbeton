from queue import Empty
from django.db import models

# Create your models here.


class Lead(models.Model):
    work_type = models.CharField(max_length=255, default='other')
    surface = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default='null')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    message = models.CharField(max_length=3000)
