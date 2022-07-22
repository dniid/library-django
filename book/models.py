from django.db import models


class Book(models.Model):
    nome = models.CharField(max_length=255)
    data_criacao = models.DateField(auto_now_add=True)
    numero_pagina = models.PositiveIntegerField(default=0)
    produtora = models.CharField(max_length=255)

    class Meta:
        db_table = "book"
