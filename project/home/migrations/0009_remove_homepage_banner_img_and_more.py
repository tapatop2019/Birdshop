# Generated by Django 5.0.6 on 2024-08-25 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_banner_img_2_homepage_banner_img_3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_img',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_img_2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_img_3',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_img_4',
        ),
    ]