# Generated by Django 3.1.1 on 2020-09-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0015_remove_game_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
