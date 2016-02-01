# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0018_groupe_groupemember_groupepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='recolte',
            field=models.IntegerField(null=True),
        ),
    ]
