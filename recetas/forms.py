from django import forms
from django.forms import ModelForm
from .models import Recetas

#Create posdatas form
class RecetaForm(ModelForm):
	class Meta:
		model = Recetas
		fields = ('nombre', 'porcion', 'tiempo', 'image', 'body')

		widget = {
			'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nombre de la receta', 'size': '40', 'width': '100%'}),
			'porcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '¿Cuantas porciones rinde?'}),
			'tiempo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tiempo de preparación'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tu nombre'}),
		}
