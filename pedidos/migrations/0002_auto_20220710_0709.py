# Generated by Django 3.0 on 2022-07-10 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineaspedidos',
            old_name='produtos',
            new_name='productos',
        ),
    ]