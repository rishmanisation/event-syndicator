# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_synd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=140)),
                ('event_description', models.CharField(max_length=1000)),
                ('event_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('event_start_date_time', models.DateTimeField()),
                ('event_end_date_time', models.DateTimeField()),
                ('is_syndicated', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
