# Generated by Django 3.0.4 on 2020-05-24 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('whynote', '0004_auto_20200516_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 5, 24, 15, 1, 49, 51599, tzinfo=utc), help_text='Use the following format: YYYY-MM-DD', verbose_name='Day of the event'),
        ),
        migrations.AlterField(
            model_name='note',
            name='public_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 15, 1, 49, 49573, tzinfo=utc), verbose_name='The publication date'),
        ),
    ]
