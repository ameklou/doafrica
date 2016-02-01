# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0022_auto_20160130_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2016, 1, 30, 19, 58, 30, 973687, tzinfo=utc), to='doafrica.Profil'),
            preserve_default=False,
        ),
    ]
