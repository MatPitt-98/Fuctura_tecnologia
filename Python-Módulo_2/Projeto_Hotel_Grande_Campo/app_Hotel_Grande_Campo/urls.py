from django.urls import path
from django.contrib import admin
from .views import * 

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('clientes/', clientes_view, name='clientes'),
    path('clientes/criar/', criar_cliente, name='criar_cliente'),
    path('reservas/', reservas_view, name='reservas'),
    path('reservas/criar/', criar_reserva, name='criar_reserva'),
]
