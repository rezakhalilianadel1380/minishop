# Generated by Django 4.2.2 on 2023-07-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_slug_url_alter_productvarient_color_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(upload_to='products_gallery/'),
        ),
        migrations.AlterField(
            model_name='productvarient',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=13),
        ),
    ]