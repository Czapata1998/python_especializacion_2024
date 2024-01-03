from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import prueba
# Create your views here.


class indexView(TemplateView):
    template_name = 'home/index.html'
    
class pruebaListView(ListView):
    template_name = 'home/list.html'
    queryset = ['A', 'B', 'C', 'D']
    context_object_name = 'listar_array'
    
class ModelListView(ListView):
    model = prueba
    template_name = "prueba_list.html"
    context_object_name = "lista_prueba"
