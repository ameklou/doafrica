# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0007_auto_20160113_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 13, 1, 28, 50, 462703, tzinfo=utc)),
        ),
    ]
