# Generated by Django 3.0.2 on 2020-03-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200304_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='tell',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='main',
            name='set_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.CharField(max_length=100),
        ),
    ]
