# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0013_auto_20160120_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postentrepreneur',
            name='montant',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='postentrepreneur',
            name='recolte',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 20, 19, 4, 55, 373300, tzinfo=utc)),
        ),
    ]
