# Generated by Django 2.1.7 on 2022-07-22 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_auto_20220722_1653'),
        ('catalog', '0002_auto_20220722_1627'),
        ('book', '0003_auto_20220722_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='catalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Catalog'),
        ),
    ]
