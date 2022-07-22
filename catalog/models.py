from django.db import models


class Catalog(models.Model):
    cname = models.CharField(max_length=255)
    cdate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "catalog"
