from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Recetas
from .forms import RecetaForm

# Create your views here.
class home(ListView):
    model = Recetas
    template_name = 'home.html'
    recetas = Recetas.objects.all()

class publicar(CreateView):
    model = Recetas
    template_name = 'receta_form.html'
    form_class = RecetaForm

def nosotros(request):
	return render(request, 'about.html')