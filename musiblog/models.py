from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Categories(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("inicio")
    
class Post(models.Model):
    titulo= models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    titulo_tag= models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_post = models.DateField(auto_now_add=True)
    category= models.CharField(max_length=255, default='music')

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse("inicio")
    
class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    imagen_perfil = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("inicio")
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.post.titulo} - {self.name}'

