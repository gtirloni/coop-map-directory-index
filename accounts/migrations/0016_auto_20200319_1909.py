# Generated by Django 3.0.3 on 2020-03-19 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200319_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Source'),
            preserve_default=False,
        ),
    ]