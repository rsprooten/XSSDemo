from django.db import models

# Create your models here.

class levelEen(models.Model):
    bericht = models.TextField()
    naam = models.CharField(max_length=255)
    host = models.CharField(max_length=255, default='127.0.0.1:8000')

class levelTwee(models.Model):
    bericht = models.TextField()
    naam = models.CharField(max_length=255)
    host = models.CharField(max_length=255, default='127.0.0.1:8000')

class levelDrie(models.Model):
    bericht = models.TextField()
    naam = models.CharField(max_length=255)
    host = models.CharField(max_length=255, default='127.0.0.1:8000')

class levelVier(models.Model):
    bericht = models.TextField()
    naam = models.CharField(max_length=255)
    host = models.CharField(max_length=255, default='127.0.0.1:8000')