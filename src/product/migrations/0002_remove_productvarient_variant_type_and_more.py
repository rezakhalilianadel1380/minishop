# Generated by Django 4.2.2 on 2023-07-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvarient',
            name='variant_type',
        ),
        migrations.AddField(
            model_name='product',
            name='product_varient',
            field=models.CharField(blank=True, choices=[('color', 'رنگ'), ('size', 'اندازه')], max_length=50, null=True),
        ),
    ]