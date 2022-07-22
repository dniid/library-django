from django.db import models


class Author(models.Model):
    nome = models.CharField(max_length=255)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "author"
