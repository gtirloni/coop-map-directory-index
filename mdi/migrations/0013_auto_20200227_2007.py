# Generated by Django 3.0.3 on 2020-02-27 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0012_tool_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='license',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mdi.License'),
        ),
    ]
