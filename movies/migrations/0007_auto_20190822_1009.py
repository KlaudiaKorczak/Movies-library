# Generated by Django 2.2.3 on 2019-08-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20190822_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='Ratings',
            field=models.ManyToManyField(to='movies.Ratings'),
        ),
    ]
