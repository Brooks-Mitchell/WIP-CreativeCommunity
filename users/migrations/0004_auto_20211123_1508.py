# Generated by Django 3.2.9 on 2021-11-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_yoe',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_bio',
            field=models.TextField(blank=True, default=''),
        ),
    ]
