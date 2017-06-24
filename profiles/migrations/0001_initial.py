# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=32)),
                ('middleInitial', models.CharField(max_length=1)),
                ('lastName', models.CharField(max_length=64)),
                ('phoneNumber', models.CommaSeparatedIntegerField(max_length=11)),
                ('street', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=12)),
                ('zipcode', models.CharField(max_length=10)),
                ('relation', models.CharField(choices=[('ga', 'Guardian'), ('sp', 'Spouse'), ('fa', 'Father'), ('mo', 'Mother'), ('si', 'Sibling'), ('ch', 'Child'), ('ot', 'Other'), ('se', 'Self')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='HealthNetUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountType', models.CharField(choices=[('P', 'Patient'), ('D', 'Doctor'), ('A', 'Admin'), ('N', 'Nurse')], default='P', max_length=1)),
                ('isNew', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('healthnetuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.HealthNetUser')),
                ('birthDate', models.DateField()),
                ('heightFeet', models.IntegerField()),
                ('heightInches', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('insuranceCompany', models.CharField(max_length=200)),
                ('insuranceId', models.CharField(max_length=200)),
                ('hospitalPref', models.CharField(max_length=200)),
                ('allergies', models.TextField()),
                ('conditions', models.TextField()),
                ('prescriptions', models.TextField()),
            ],
            bases=('profiles.healthnetuser',),
        ),
        migrations.AddField(
            model_name='healthnetuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.HealthNetUser'),
        ),
    ]
