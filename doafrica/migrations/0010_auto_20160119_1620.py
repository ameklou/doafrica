# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0009_auto_20160119_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='business_card',
            field=models.ImageField(default=datetime.datetime(2016, 1, 19, 16, 20, 46, 109971, tzinfo=utc), max_length=255, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profil',
            name='id_card',
            field=models.ImageField(default=datetime.datetime(2016, 1, 19, 16, 20, 59, 825161, tzinfo=utc), max_length=255, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profil',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 16, 20, 25, 506307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 16, 20, 25, 497063, tzinfo=utc)),
        ),
    ]
