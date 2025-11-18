from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('excluir/<int:id>/', views.excluir_livro, name='excluir_livro'),
    path('editar/<int:id>/', views.editar_livro, name='editar_livro'),
]
