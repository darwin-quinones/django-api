from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    wedsite = models.URLField(max_length=100)
    fundation = models.PositiveIntegerField()
    