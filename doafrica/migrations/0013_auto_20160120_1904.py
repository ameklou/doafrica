# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0012_auto_20160120_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='register_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 20, 19, 4, 4, 333424, tzinfo=utc)),
        ),
    ]
