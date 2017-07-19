# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=64)),
                ('enabled', models.BooleanField(default=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=64)),
                ('enabled', models.BooleanField(default=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('temperature', models.FloatField()),
                ('deployment', models.ForeignKey(to='sensorhub.Deployment', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('serial_number', models.CharField(max_length=16)),
                ('enabled', models.BooleanField(default=True, db_index=True)),
                ('deployment', models.ForeignKey(to='sensorhub.Deployment', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='reading',
            name='sensor',
            field=models.ForeignKey(to='sensorhub.Sensor', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='deployment',
            name='location',
            field=models.ForeignKey(to='sensorhub.Location', on_delete=models.CASCADE),
        ),
    ]
