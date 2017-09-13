# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Pictures',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, to='cms.CMSPlugin', serialize=False, primary_key=True, auto_created=True, related_name='photoblog_plugins_my_pictures')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='my_pictures')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'My Picture',
                'verbose_name_plural': 'My Pictures',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
