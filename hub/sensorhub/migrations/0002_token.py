# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensorhub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=64)),
                ('api_key', models.CharField(editable=False, max_length=16, unique=True)),
                ('api_secret', models.CharField(editable=False, max_length=16)),
                ('enabled', models.BooleanField(db_index=True, default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterIndexTogether(
            name='token',
            index_together={('api_key', 'api_secret')},
        ),
    ]
