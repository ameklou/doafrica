# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doafrica', '0016_auto_20160122_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date_de_pub', models.DateField(auto_now_add=True)),
                ('montant', models.IntegerField()),
                ('categorie', models.CharField(max_length=1, choices=[(b'A', b'commercial'), (b'B', b'agricole'), (b'C', b'servie'), (b'D', b'social')])),
                ('image', models.ImageField(upload_to=b'projet')),
                ('recolte', models.IntegerField()),
                ('valide', models.CharField(max_length=5, null=True)),
                ('post_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='PostEntrepreneur',
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=b'documents/'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='register_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
