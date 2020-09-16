# Generated by Django 3.1.1 on 2020-09-15 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0004_review_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='game',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='gaming.game'),
        ),
    ]