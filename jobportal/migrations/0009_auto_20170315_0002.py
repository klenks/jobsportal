# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0008_remove_person_join_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]