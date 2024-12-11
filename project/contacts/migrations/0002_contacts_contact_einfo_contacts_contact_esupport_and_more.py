# Generated by Django 5.0.6 on 2024-08-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='contact_einfo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_esupport',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_numberstreet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_phone_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_phone_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_text_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='contact_text_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]