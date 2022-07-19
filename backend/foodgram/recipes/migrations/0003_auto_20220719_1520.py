# Generated by Django 2.2.16 on 2022-07-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20220718_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(default='cccccc', max_length=6, unique=True, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
    ]
