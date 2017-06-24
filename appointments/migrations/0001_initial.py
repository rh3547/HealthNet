# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('startDate', models.DateField()),
                ('startTime', models.CharField(max_length=10)),
                ('endDate', models.DateField()),
                ('endTime', models.CharField(max_length=10)),
                ('doctor', models.CharField(max_length=96)),
                ('hospital', models.CharField(max_length=64)),
                ('room', models.CharField(max_length=32)),
                ('reason', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Patient')),
            ],
        ),
    ]
