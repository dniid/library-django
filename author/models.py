from django.db import models


class Author(models.Model):
    aname = models.CharField(max_length=255)
    adate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "author"
