from django.db import models

# Create your models here.


class Livro(models.Model):
    STATUS_CHOICES = [
        ('EP', 'Em progresso'),
        ('L', 'Lido'),
    ]

    nome = models.CharField(max_length=200)
    escritor = models.CharField(max_length=200)
    editora = models.CharField(max_length=200)
    progresso = models.IntegerField(default=0)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='EP')
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.status == 'L':
            self.progresso = 100

        elif self.progresso > 99.99:
            self.progresso = 99.99

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
