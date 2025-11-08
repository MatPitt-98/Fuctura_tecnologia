from django.urls import path
from django.contrib import admin
from .views import (
    login_view, logout_view,
    register_view, dashboard,
    criar_cliente, clientes_view,
    criar_reserva, reservas_view,
)

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
