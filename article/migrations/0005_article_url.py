# Generated by Django 3.1.5 on 2021-01-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]