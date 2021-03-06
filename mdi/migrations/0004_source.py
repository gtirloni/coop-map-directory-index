# Generated by Django 3.0.3 on 2020-02-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0003_auto_20200213_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ioo.coop/directory/', max_length=255, unique=True)),
                ('description', models.CharField(blank=True, default='The Internet of Ownership #PlatformCoop Directory', max_length=255)),
                ('url', models.CharField(blank=True, default='http://ioo.coop/directory/', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
