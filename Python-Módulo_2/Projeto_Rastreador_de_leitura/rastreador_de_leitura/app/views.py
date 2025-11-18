from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.core.paginator import Paginator

# Create your views here.


def lista_livros(request):
    ordering = request.GET.get("ordering", "nome")
    livros = Livro.objects.all().order_by(ordering)
    paginator = Paginator(livros, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/lista.html', {'livros': livros, 'page_obj': page_obj, 'ordering': ordering})


def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'app/formulario.html', {'form': form})


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('lista_livros')

def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)

    return render(request, 'app/formulario.html', {'form': form})