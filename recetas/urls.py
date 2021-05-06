from django.urls import path
from .views import home, publicar, nosotros, buscar, detail

urlpatterns = [
	path('', home.as_view(), name='home'),
	path('publicar', publicar.as_view(), name='publicar'),
	path('nosotros', nosotros, name='nosotros'),
	path('buscar', buscar, name='buscar'),
	path('detail', detail.as_view(), name='detail'),
]