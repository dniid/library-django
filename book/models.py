from django.db import models


class Book(models.Model):
    bname = models.CharField(max_length=255)
    bdate = models.DateField(auto_now_add=True)
    bnumpag = models.CharField(max_length=255)
    bprod = models.CharField(max_length=255)

    class Meta:
        db_table = "book"
