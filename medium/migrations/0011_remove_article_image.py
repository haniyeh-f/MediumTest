# Generated by Django 3.1.6 on 2021-02-06 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0010_auto_20210206_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]
