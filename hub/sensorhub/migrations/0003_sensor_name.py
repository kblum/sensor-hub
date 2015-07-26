# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensorhub', '0002_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='name',
            field=models.CharField(default='N/A', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='token',
            name='api_key',
            field=models.CharField(editable=False, unique=True, max_length=16, verbose_name='API key'),
        ),
        migrations.AlterField(
            model_name='token',
            name='api_secret',
            field=models.CharField(editable=False, max_length=16, verbose_name='API secret'),
        ),
    ]
