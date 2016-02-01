# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='busness_card',
            field=models.ImageField(max_length=255, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='id_card',
            field=models.ImageField(max_length=255, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='photo',
            field=models.ImageField(max_length=255, upload_to=b''),
        ),
    ]
