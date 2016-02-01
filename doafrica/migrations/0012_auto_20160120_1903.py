# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doafrica', '0011_auto_20160119_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostEntrepreneur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date_de_pub', models.DateField(auto_now_add=True)),
                ('montant', models.IntegerField(max_length=20)),
                ('categorie', models.CharField(max_length=1, choices=[(b'A', b'commercial'), (b'B', b'agricole'), (b'C', b'servie'), (b'D', b'social')])),
                ('image', models.ImageField(upload_to=b'projet')),
                ('recolte', models.IntegerField(max_length=20)),
                ('valide', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profil',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 20, 19, 3, 6, 463191, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 20, 19, 3, 6, 453316, tzinfo=utc)),
        ),
    ]
