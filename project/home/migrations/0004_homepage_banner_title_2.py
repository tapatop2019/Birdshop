# Generated by Django 5.0.6 on 2024-06-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title_2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]