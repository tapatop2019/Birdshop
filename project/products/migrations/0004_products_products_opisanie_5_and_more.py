# Generated by Django 5.0.6 on 2024-07-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_products_opisanie_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='products_opisanie_5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='products_opisanie_6',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='products_opisanie_7',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='products_opisanie_8',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
