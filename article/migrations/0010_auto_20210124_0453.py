# Generated by Django 3.1.5 on 2021-01-23 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20210124_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, default=None, max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='book',
            field=models.CharField(blank=True, default=None, max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='conference',
            field=models.CharField(blank=True, default=None, max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='issue',
            field=models.CharField(blank=True, default=None, max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='journal',
            field=models.CharField(blank=True, default=None, max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='page',
            field=models.CharField(blank=True, default=None, max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publisher',
            field=models.CharField(blank=True, default=None, max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=6000),
        ),
    ]
