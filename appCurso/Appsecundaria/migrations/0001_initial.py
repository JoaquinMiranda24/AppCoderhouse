# Generated by Django 5.0.3 on 2024-03-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Articulo', models.CharField(max_length=40)),
                ('Descripcion', models.CharField(max_length=40)),
                ('Precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]
