from django.db import models

# Create your models here.


class Quarto(models.Model):
    numero = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_de_entrada = models.DateField()
    data_de_saida = models.DateField()

    def __str__(self):
        return f'Reserva de {self.cliente} no quarto {self.quarto}, entrada em {self.data_de_entrada} e saída em {self.data_de_saida}.'


class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f'{self.descricao} - {self.valor}'


class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f'{self.descricao} - {self.valor}'
