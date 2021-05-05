from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Recetas(models.Model):
	nombre = models.CharField(max_length=200)
	porcion = models.CharField(max_length=200)
	tiempo = models.CharField(max_length=200)
	fecha = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(null=True)
	body = RichTextField(blank=True, null=True)
	autor = models.CharField(max_length=200, null=True)
	

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('home')