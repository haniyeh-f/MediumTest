# Generated by Django 3.1.6 on 2021-02-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0009_auto_20210206_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.URLField(max_length=255),
        ),
    ]