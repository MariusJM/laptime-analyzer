# Generated by Django 5.1.2 on 2024-11-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_tracklayout'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracklayout',
            name='thumbnail_url',
            field=models.URLField(blank=True, null=True, verbose_name='Thumbnail URL'),
        ),
    ]
