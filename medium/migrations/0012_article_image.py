# Generated by Django 3.1.6 on 2021-02-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0011_remove_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.URLField(default=''),
        ),
    ]
