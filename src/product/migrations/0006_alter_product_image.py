# Generated by Django 4.2.2 on 2023-07-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productvarient_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
