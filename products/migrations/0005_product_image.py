# Generated by Django 3.0.7 on 2020-07-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to='products/images/'),
        ),
    ]
