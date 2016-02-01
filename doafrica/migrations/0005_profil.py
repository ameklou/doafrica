# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doafrica', '0004_auto_20160111_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telephone', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('biography', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
                ('twitter', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('photo', models.ImageField(max_length=255, upload_to=b'')),
                ('account', models.CharField(max_length=1, choices=[(b'A', b'Entrepreneur'), (b'B', b'Cabinet'), (b'C', b'Investisseur')])),
                ('activated', models.CharField(max_length=5, null=True)),
                ('active', models.CharField(max_length=5, null=True)),
                ('premium', models.CharField(max_length=1, choices=[(b'A', b'Free'), (b'B', b'Argent'), (b'C', b'Gold')])),
                ('register_date', models.DateField()),
                ('id_card', models.ImageField(max_length=255, upload_to=b'')),
                ('busness_card', models.ImageField(max_length=255, upload_to=b'')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
