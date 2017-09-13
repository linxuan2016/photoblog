# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('photoblog_plugins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='photoblog_plugins_hello', to='cms.CMSPlugin', parent_link=True)),
                ('guest_name', models.CharField(default='Guest', max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
