# Generated by Django 5.0.6 on 2024-08-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_homepage_banner_title_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
