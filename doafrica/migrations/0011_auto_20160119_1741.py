# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0010_auto_20160119_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='business_card',
            field=models.ImageField(upload_to=b'photo/'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='id_card',
            field=models.ImageField(upload_to=b'photo/'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='photo',
            field=models.ImageField(upload_to=b'photo/'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 17, 41, 29, 401043, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 19, 17, 41, 29, 391572, tzinfo=utc)),
        ),
    ]
