# Generated by Django 5.0.6 on 2024-08-29 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('blog_opisanie_1', models.CharField(blank=True, max_length=100, null=True)),
                ('blog_opisanie_2', models.CharField(blank=True, max_length=100, null=True)),
                ('blog_opisanie_3', models.CharField(blank=True, max_length=100, null=True)),
                ('blog_opisanie_4', models.CharField(blank=True, max_length=100, null=True)),
                ('blog_img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
