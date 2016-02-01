# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0002_auto_20160111_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
