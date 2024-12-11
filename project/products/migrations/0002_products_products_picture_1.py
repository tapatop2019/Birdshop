# Generated by Django 5.0.6 on 2024-07-05 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='products_picture_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
