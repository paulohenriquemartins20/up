from django.db import models

# Create your models here.

class usuarios(models.Model):

    ti = models.TextField(max_length=20)
    cpf = models.TextField(max_length=20)
    numero = models.TextField(max_length=20)
    vali = models.TextField(max_length=20)
    cod = models.TextField(max_length=20)