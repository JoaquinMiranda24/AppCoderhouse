# Generated by Django 5.0.3 on 2024-03-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appsecundaria', '0002_remove_vender_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('clave', models.IntegerField()),
            ],
        ),
    ]