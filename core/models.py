from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True)
    senha = models.CharField(max_length=12)

    def __str__(self):
        return self.nome
