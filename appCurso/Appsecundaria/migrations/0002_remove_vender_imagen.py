# Generated by Django 5.0.3 on 2024-03-31 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appsecundaria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vender',
            name='imagen',
        ),
    ]
