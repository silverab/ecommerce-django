# Generated by Django 3.0.7 on 2020-07-15 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200715_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
