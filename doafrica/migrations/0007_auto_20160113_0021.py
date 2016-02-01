# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0006_auto_20160112_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='busness_card',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='id_card',
        ),
        migrations.AlterField(
            model_name='profil',
            name='telephone',
            field=models.IntegerField(null=True),
        ),
    ]
