# Generated by Django 2.0.8 on 2019-03-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0017_auto_20190227_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcotizacion',
            name='lugdestino',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dcotizacion',
            name='lugorigen',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dgasto',
            name='lugdestino',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dgasto',
            name='lugorigen',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dguia',
            name='lugdestino',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dguia',
            name='lugorigen',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
