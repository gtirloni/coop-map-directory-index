# Generated by Django 3.0.3 on 2020-03-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0027_auto_20200302_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]
