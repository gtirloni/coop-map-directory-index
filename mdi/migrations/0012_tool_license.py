# Generated by Django 3.0.3 on 2020-02-27 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0011_auto_20200227_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='license',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mdi.License'),
            preserve_default=False,
        ),
    ]
