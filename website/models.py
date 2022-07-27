from cgitb import text
from email.mime import image
from logging import makeLogRecord
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
class Buy(models.Model):
    reklama = models.CharField(max_length=100)
    sarlavha = models.CharField(max_length=100)
    text = models.TextField(max_length=100)
    chegirma_narx = models.IntegerField()
    asl_narx = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self):
        return self.reklama

class Discover(models.Model):
    arm_chair = models.CharField(max_length=100)
    text = models.TextField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.arm_chair