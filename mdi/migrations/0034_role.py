# Generated by Django 3.0.3 on 2020-03-22 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0033_auto_20200320_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('order', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
