# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorhub', '0004_deployment_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('user_agent_string', models.TextField(unique=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='reading',
            name='user_agent',
            field=models.ForeignKey(blank=True, null=True, to='sensorhub.UserAgent', on_delete=models.SET_NULL),
        ),
    ]
