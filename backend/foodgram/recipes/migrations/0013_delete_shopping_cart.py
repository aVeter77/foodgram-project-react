# Generated by Django 3.2.14 on 2022-07-31 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_delete_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shopping_cart',
        ),
    ]
