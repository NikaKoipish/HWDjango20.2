# Generated by Django 5.0.3 on 2024-04-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество просмотров'),
        ),
    ]
