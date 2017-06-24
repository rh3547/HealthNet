# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=64)),
                ('action', models.CharField(max_length=64)),
                ('eventCode', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]
