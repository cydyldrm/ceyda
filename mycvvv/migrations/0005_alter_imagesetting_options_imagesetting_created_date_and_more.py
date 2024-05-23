# Generated by Django 5.0.3 on 2024-05-23 12:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycvvv', '0004_imagesetting_alter_generalsetting_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesetting',
            options={'ordering': ('name',), 'verbose_name': 'Image Setting', 'verbose_name_plural': 'Image Settings'},
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated date'),
        ),
    ]