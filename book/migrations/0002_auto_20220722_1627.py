# Generated by Django 2.1.7 on 2022-07-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bdate',
            new_name='data_criacao',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='bname',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='bprod',
            new_name='produtora',
        ),
        migrations.RemoveField(
            model_name='book',
            name='bnumpag',
        ),
        migrations.AddField(
            model_name='book',
            name='numero_pagina',
            field=models.PositiveIntegerField(default=0),
        ),
    ]