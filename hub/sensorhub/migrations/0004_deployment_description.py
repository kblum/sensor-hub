# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensorhub', '0003_sensor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
