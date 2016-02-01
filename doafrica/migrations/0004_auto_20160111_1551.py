# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0003_auto_20160111_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='address',
            field=models.CharField(default=datetime.datetime(2016, 1, 11, 15, 50, 52, 115014, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='country',
            field=models.CharField(default=datetime.datetime(2016, 1, 11, 15, 51, 13, 688465, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
