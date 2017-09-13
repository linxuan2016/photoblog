# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('photoblog_plugins', '0002_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hello',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='Hello',
        ),
    ]
