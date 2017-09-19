# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('photoblog_plugins', '0003_auto_20170913_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Link',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, to='cms.CMSPlugin', auto_created=True, related_name='photoblog_plugins_image_link', parent_link=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image_link')),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Image Link',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
