# models.py

from django.db import models

class Contacto(models.Model):
    name = models.CharField(max_length=100), 
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    menssaje = models.TextField()
 