from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, blank=True)

