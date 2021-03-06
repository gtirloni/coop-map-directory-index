# Generated by Django 3.0.3 on 2020-05-11 18:14

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0065_auto_20200508_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='founded_max_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='founded_min_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='geo_scope',
            field=models.CharField(blank=True, choices=[(0, 'Local'), (1, 'Regional'), (2, 'National'), (3, 'International')], max_length=16, verbose_name='Geographic scope'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='geo_scope_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Geographic scope – City'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='geo_scope_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Geographic scope – Country'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='geo_scope_region',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Geographic scope – Region'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='num_workers',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of workers'),
        ),
    ]
