from django.urls import path
from .views import home, publicar, nosotros, buscar, receta
from recetas import views

urlpatterns = [
	path('', home, name='home'),
	path('publicar', publicar.as_view(), name='publicar'),
	path('nosotros', nosotros, name='nosotros'),
	path('buscar', views.buscar, name='buscar'),
	path('receta/<receta_id>', views.receta, name='receta'),
]