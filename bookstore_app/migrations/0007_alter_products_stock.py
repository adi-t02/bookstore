# Generated by Django 5.2 on 2025-05-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0006_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
