from django.contrib import admin
from django.urls import path, include
from .views import home, cadastro, editar, atualizar

urlpatterns = [
    path('', home),
    path('cadastro/', cadastro, name="cadastro"),
    path('editar/<int:id>', editar, name="editar"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),
]