# Generated by Django 3.0.3 on 2020-03-23 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0036_tool_sectors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
