# Generated by Django 5.0.3 on 2024-04-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='признак активности версии'),
        ),
    ]
