# Generated by Django 3.0.3 on 2020-04-24 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_remove_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_profile',
            field=models.BooleanField(default=False),
        ),
    ]
