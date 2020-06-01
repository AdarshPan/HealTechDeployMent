from django.db import models

# Create your models here.
class Members(models.Model):
    name=models.CharField(max_length=250)