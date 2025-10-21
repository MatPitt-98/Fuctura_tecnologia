from django.urls import path
from django.contrib import admin
from .views import (
                    relatorios_view, criar_agendamento,
                    criar_cliente, criar_servico,
                    register_view, logout_view,
                    login_view, servicos_view,
                    dashboard, clientes_view, agendamentos_view,
)

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('clientes/', clientes_view, name='clientes'),
    path('clientes/criar/', criar_cliente, name='criar_cliente'),
    path('servicos/criar/', criar_servico, name='criar_servico'),
    path('agendamentos/', agendamentos_view, name='agendamentos'),
    path('agendamentos/criar/', criar_agendamento, name='criar_agendamento'),
    path('relatorios/', relatorios_view, name='relatorios'),
]
