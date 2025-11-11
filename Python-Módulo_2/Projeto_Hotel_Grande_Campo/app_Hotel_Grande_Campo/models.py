from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Quarto(models.Model):
    TIPOS_DE_QUARTO = [
        ('basico', 'Básico'),
        ('superior', 'Superior'),
        ('luxo', 'Luxo'),
        ('suite', 'Suíte'),
        ('executivo', 'Executivo'),
    ]

    numero = models.CharField(max_length=4)
    tipo = models.CharField(max_length=20, choices=TIPOS_DE_QUARTO, default='basico')
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'Quarto: {self.numero} - {self.get_tipo_display()}'


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_entrada = models.DateField()
    data_saida = models.DateField()

    def __str__(self):
        return f'Cliente: {self.cliente.nome}, Quarto: {self.quarto.numero}'


class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f'{self.descricao} - R$ {self.valor:.2f}'


class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f'{self.descricao} - R$ {self.valor:.2f}'
