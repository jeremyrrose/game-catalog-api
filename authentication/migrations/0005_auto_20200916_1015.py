# Generated by Django 3.1.1 on 2020-09-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0008_auto_20200916_1015'),
        ('authentication', '0004_auto_20200915_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='games',
            field=models.ManyToManyField(blank=True, default=None, related_name='owned', to='gaming.Game'),
        ),
        migrations.AlterField(
            model_name='user',
            name='watch_list',
            field=models.ManyToManyField(blank=True, default=None, related_name='watcher', to='gaming.Game'),
        ),
    ]