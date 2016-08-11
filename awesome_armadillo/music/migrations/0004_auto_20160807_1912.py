# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-07 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
