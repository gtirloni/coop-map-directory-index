# Generated by Django 3.0.3 on 2020-03-20 19:40

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200319_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': [django.db.models.functions.text.Lower('email')]},
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='user',
            name='source',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='accounts.Source'),
        ),
    ]
