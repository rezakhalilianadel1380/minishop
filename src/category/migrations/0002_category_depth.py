# Generated by Django 4.2.2 on 2023-07-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='depth',
            field=models.IntegerField(default=0),
        ),
    ]