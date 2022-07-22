from django.db import models
from author.models import Author
from catalog.models import Catalog


class Book(models.Model):
    nome = models.CharField(max_length=255)
    data_criacao = models.DateField(auto_now_add=True)
    numero_pagina = models.PositiveIntegerField(default=1)
    produtora = models.CharField(max_length=255)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "book"
