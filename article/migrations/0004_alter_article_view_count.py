# Generated by Django 5.0.3 on 2024-04-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
