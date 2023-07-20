# Generated by Django 4.2.2 on 2023-07-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productvarient_is_deafult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_brief',
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_fa',
            field=models.CharField(max_length=100, null=True),
        ),
    ]