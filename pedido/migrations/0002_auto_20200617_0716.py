# Generated by Django 2.2.4 on 2020-06-17 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itempedido',
            old_name='preço',
            new_name='preco',
        ),
    ]
