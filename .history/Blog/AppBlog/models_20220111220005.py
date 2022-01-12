from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    website = models.URLField()
    company = models.CharField(max_length=100)
    about = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return f"USUARIO: {self.name} EMAIL: {self.email} PHONE: {self.phone} ADDRESS: {self.address} CITY: {self.city} STATE: {self.state} ZIP: {self.zip} WEBSITE: {self.website} COMPANY: {self.company} ABOUT: {self.about} CREATED_AT: {self.created_at} UPDATED_AT: {self.updated_at}"
    
class Posteo(models.Model):
    titulo = models.CharField(max_length=100)
    numero = models.IntegerField()
    descripcion = models.TextField(max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()
    
    def __str__(self):
        return f"POSTEO: {self.titulo} NUMERO: {self.numero} DESCRIPTION: {self.descripcion} USUARIO: {self.usuario} CREATED_AT: {self.creado} UPDATED_AT: {self.actualizado}"
    
