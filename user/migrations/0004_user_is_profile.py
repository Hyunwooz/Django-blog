# Generated by Django 4.2.3 on 2023-07-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_avatarurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_profile',
            field=models.BooleanField(default=False),
        ),
    ]
