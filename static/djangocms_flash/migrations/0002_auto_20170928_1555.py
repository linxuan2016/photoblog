# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_flash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flash',
            name='cmsplugin_ptr',
            field=models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, serialize=False, related_name='djangocms_flash_flash', to='cms.CMSPlugin'),
        ),
    ]
