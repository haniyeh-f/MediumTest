# Generated by Django 3.1.6 on 2021-02-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0006_article_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]