# Generated by Django 4.0 on 2022-01-11 07:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='datacreated',
        ),
        migrations.AddField(
            model_name='tasks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 7, 10, 56, 679640, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
