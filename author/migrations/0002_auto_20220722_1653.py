# Generated by Django 2.1.7 on 2022-07-22 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='adate',
            new_name='data_criacao',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='aname',
            new_name='nome',
        ),
    ]
