# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20141020_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='status',
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='friend',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='user',
            field=models.CharField(max_length=128),
        ),
    ]
