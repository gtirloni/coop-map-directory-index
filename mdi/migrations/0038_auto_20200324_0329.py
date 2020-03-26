# Generated by Django 3.0.3 on 2020-03-24 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0037_auto_20200323_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='mdi.Category'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_orig', to='mdi.Category'),
        ),
    ]