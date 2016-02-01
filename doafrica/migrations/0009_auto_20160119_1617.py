# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0008_auto_20160113_0128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='busness_card',
            new_name='business_card',
        ),
        migrations.AlterField(
            model_name='profil',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 16, 17, 32, 609950, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 16, 17, 32, 600548, tzinfo=utc)),
        ),
    ]
