from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Player(models.Model):
    nombre = models.CharField(max_length = 40)
    posicion = models.CharField(max_length = 15)
    pais = models.CharField(max_length = 20)
    equipo = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.nombre}"



class Team(models.Model):
    nombre = models.CharField(max_length = 30)
    pais = models.CharField(max_length = 20)
    liga = models.CharField(max_length= 30)
    division = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
class League(models.Model):
    nombre = models.CharField(max_length = 25)
    pais = models.CharField(max_length = 25)
    division = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre}"


class Tourn(models.Model):
    nombre = models.CharField(max_length = 30)
    equipos = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre}"

    

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="images", null=True, blank=True)

