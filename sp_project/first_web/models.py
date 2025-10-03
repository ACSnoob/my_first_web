from django.db import models

# Create your models here.
class Memberinfo(models.Model):
    name = models.CharField(max_length=32)
    department = models.CharField(max_length=64)
    join_time = models.CharField(max_length=128)
class PwdSaveInfo(models.Model):
    user= models.CharField(max_length=128)
    pwd = models.CharField(max_length=128)