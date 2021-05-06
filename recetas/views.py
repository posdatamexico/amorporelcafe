from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
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

class detail(DetailView):
	model = Recetas
	template_name = 'detalle.html'

	def get_context_data(self, *args, **kwargs):
		context = super(Detail, self).get_context_data(*args, **kwargs)
		stuff = get_object_or_404(Receta, id=self.kwargs['pk'])
		return context

def buscar(request):
	if request.method == "POST":
		searched = request.POST['searched']
		recetas = Recetas.objects.filter(nombre__contains=searched)
		return render(request, 'recetas.html', {'searched':searched, 'recetas':recetas})
	else:
		return render(request, 'recetas.html')