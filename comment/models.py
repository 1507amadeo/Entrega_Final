from django.conf import settings
from django.db import models


# Create your models here.
class Comentario(models.Model):
    descripcion=models.CharField(max_length=200)  
    autor=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)
    post=models.ForeignKey('post.Post',on_delete=models.CASCADE,null=True)
    fecha_publicacion=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comentario: Descripción: {self.descripcion} --- Autor:Nombre:{self.autor} --- Fecha de Publicación: {self.fecha_publicacion}'
