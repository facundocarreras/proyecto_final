from django.db import models


class Usuario (models.Model):
    name = models.CharField(max_length= 75)
    email = models.CharField(max_length= 100)
    password = models.TextField()
    imagen = models.TextField()


class Blog (models.Model):
    titulo = models.CharField(max_length = 200) 
    imagen = models.TextField()
    introduccion = models.CharField(max_length = 200) 
    contenido = models.CharField(max_length = 200) 
    fecha = models.DateField()
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    

class Contacto(models.Model):
    name = models.CharField(max_length= 75)
    email = models.CharField(max_length= 100)
    telefono = models.TextField()
    motivo = models.CharField(max_length= 100)
    mensaje = models.CharField(max_length = 200) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default= 1)

