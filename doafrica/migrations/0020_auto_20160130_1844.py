# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0019_auto_20160130_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=models.CharField(max_length=1, choices=[(b'A', b'commercial'), (b'B', b'agricole'), (b'C', b'service'), (b'D', b'social')]),
        ),
    ]
