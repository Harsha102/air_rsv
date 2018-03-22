# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-22 21:15
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_rsv', '0002_auto_20180322_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Enter valid time of format HH:MM AM/PM 12hour', regex='^((1[0-2]|0?[1-9]):([0-5][0-9]) ([AaPp][Mm]))$')]),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Enter valid time of format HH:MM AM/PM 12hour', regex='^((1[0-2]|0?[1-9]):([0-5][0-9]) ([AaPp][Mm]))$')]),
        ),
        migrations.AlterField(
            model_name='intermediatestop',
            name='arrival_time',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Enter valid time of format HH:MM 24hour', regex='^((1[0-2]|0?[1-9]):([0-5][0-9]) ([AaPp][Mm]))$')]),
        ),
        migrations.AlterField(
            model_name='intermediatestop',
            name='departure_time',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Enter valid time of format HH:MM 24hour', regex='^((1[0-2]|0?[1-9]):([0-5][0-9]) ([AaPp][Mm]))$')]),
        ),
    ]
