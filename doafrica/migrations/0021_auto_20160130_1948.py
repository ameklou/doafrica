# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0020_auto_20160130_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_user',
            new_name='author',
        ),
    ]
