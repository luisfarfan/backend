# Generated by Django 2.0.8 on 2018-09-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0009_banco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='codigo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]