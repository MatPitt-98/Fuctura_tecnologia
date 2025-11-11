from django.contrib import admin
from .models import Quarto, Cliente, Reserva, Despesa, Receita

# Registre os modelos para que apareçam no painel de administração

admin.site.register(Quarto)
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Despesa)
admin.site.register(Receita)


@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'preco', 'disponivel')
    list_filter = ('disponivel', 'tipo')
