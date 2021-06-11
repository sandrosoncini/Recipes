from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Recipes(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    protein_type = models.CharField(max_length=32)



