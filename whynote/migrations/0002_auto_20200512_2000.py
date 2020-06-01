# Generated by Django 3.0.4 on 2020-05-12 17:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('whynote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 5, 12, 17, 0, 9, 154617, tzinfo=utc), help_text='Use the following format: YYYY-MM-DD', verbose_name='Day of the event'),
        ),
        migrations.AlterField(
            model_name='note',
            name='public_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 17, 0, 9, 154617, tzinfo=utc), verbose_name='The publication date'),
        ),
    ]