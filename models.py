from django.db import models

# Create your models here.
class Record(models.Model):
    nombre = models.CharField(max_length=100)
    seccion = models.CharField(max_length=100)
    casilla = models.CharField(max_length=100)
    votosmorenapvpt = models.IntegerField()
    votosmc = models.IntegerField()
    votospripanprd = models.IntegerField()
    imagen = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nombre