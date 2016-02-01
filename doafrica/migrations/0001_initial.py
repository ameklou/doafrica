# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('telephone', models.IntegerField()),
                ('biography', models.TextField()),
                ('slug', models.TextField()),
                ('twitter', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=255)),
                ('account', models.CharField(max_length=1, choices=[(b'A', b'Entrepreneur'), (b'B', b'Cabinet'), (b'C', b'Investisseur')])),
                ('activated', models.CharField(max_length=5, null=True)),
                ('active', models.CharField(max_length=5, null=True)),
                ('premium', models.CharField(max_length=1, choices=[(b'A', b'Free'), (b'B', b'Argent'), (b'C', b'Gold')])),
                ('register_date', models.DateField()),
                ('id_card', models.CharField(max_length=255)),
                ('busness_card', models.CharField(max_length=255)),
            ],
        ),
    ]
