# Generated by Django 3.1.1 on 2020-09-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0008_auto_20200916_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(default=None, null=True),
        ),
    ]
