# Generated by Django 3.0.3 on 2020-04-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20200406_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialnetwork',
            name='hint',
            field=models.CharField(max_length=64),
        ),
    ]