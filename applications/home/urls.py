from django.urls import path
from . import views

urlpatterns = [
     path('index/', views.indexView.as_view()),
     path('listar/', views.pruebaListView.as_view()),
     path('lista-prueba/', views.ModelListView.as_view()),
]
