from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import User
from .models import Quarto, Cliente, Reserva, Despesa, Receita
from .forms import QuartoForm, ClienteForm, ReservaForm, DespesaForm, ReceitaForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard') # Redireciona para o dashboard após login
    return render(request, 'app_Hotel_Grande_Campo/login.html')

def logout_view(request):
    logout(request)
    return redirect('login') # Redireciona para a página de login após logout

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'app_Hotel_Grande_Campo/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'app_Hotel_Grande_Campo/dashboard.html')

@login_required
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'app_Hotel_Grande_Campo/criar_cliente.html', {'form': form})

@login_required
def clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_Hotel_Grande_Campo/clientes.html', {'clientes': clientes})

@login_required
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm()
    return render(request, 'app_Hotel_Grande_Campo/criar_reserva.html', {'form': form})

@login_required
def reservas_view(request):
    reservas = Reserva.objects.all()
    return render(request, 'app_Hotel_Grande_Campo/reservas.html', {'reservas': reservas})
