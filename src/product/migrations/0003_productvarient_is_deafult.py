# Generated by Django 4.2.2 on 2023-07-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_productvarient_variant_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvarient',
            name='is_deafult',
            field=models.BooleanField(default=False),
        ),
    ]