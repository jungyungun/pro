# Generated by Django 2.1.5 on 2019-02-27 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MorningBriefing', '0005_remove_news_usage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Comment',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='news',
            name='Title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
