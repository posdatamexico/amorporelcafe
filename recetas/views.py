from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView
from .models import Recetas
from .forms import RecetaForm

# Create your views here.
def home(request):
	recetas = Recetas.objects.all()
	return render(request, 'home.html',
		{'recetas':recetas})

class publicar(CreateView):
	model = Recetas
	template_name = 'receta_form.html'
	form_class = RecetaForm

def nosotros(request):
	return render(request, 'about.html')

def receta(request, receta_id):
	receta = Recetas.objects.get(pk=receta_id)
	return render(request, 'detalle.html', {'receta':receta})

def buscar(request):
	if request.method == "POST":
		searched = request.POST['searched']
		recetas = Recetas.objects.filter(nombre__contains=searched)
		return render(request, 'recetas.html', {'searched':searched, 'recetas':recetas})
	else:
		return render(request, 'recetas.html',)
