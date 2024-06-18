from django.db import models

# Create your models here.

class Usuario(models.Model):

    password=models.CharField(max_length=30, unique=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField(unique=True)
    ultimo_login=models.DateTimeField(auto_now=True)

    # campo de opciones 

    OPCIONES_ROL = [
    ('personal', 'Personal'),
    ('empresa', 'Empresa'),
]

    roles=models.CharField(max_length=8, choices=OPCIONES_ROL, default='personal')