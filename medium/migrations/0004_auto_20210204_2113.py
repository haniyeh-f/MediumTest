# Generated by Django 3.1.6 on 2021-02-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0003_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
