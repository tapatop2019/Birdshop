# Generated by Django 5.0.6 on 2024-08-29 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mistake',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('mistake_opisanie_1', models.CharField(blank=True, max_length=100, null=True)),
                ('mistake_opisanie_2', models.CharField(blank=True, max_length=100, null=True)),
                ('mistake_opisanie_3', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]