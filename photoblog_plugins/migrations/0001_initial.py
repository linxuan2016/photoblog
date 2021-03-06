# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='photoblog_plugins_carousel', to='cms.CMSPlugin', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
                ('image_1', models.ImageField(upload_to='carousel')),
                ('name_1', models.CharField(max_length=200)),
                ('title_1', models.CharField(max_length=200)),
                ('text_1', models.TextField()),
                ('image_2', models.ImageField(upload_to='carousel')),
                ('name_2', models.CharField(max_length=200)),
                ('title_2', models.CharField(max_length=200)),
                ('text_2', models.TextField()),
                ('image_3', models.ImageField(upload_to='carousel')),
                ('name_3', models.CharField(max_length=200)),
                ('title_3', models.CharField(max_length=200)),
                ('text_3', models.TextField()),
            ],
            options={
                'verbose_name': 'Carousel',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Footer_New',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='photoblog_plugins_footer_new', to='cms.CMSPlugin', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
                ('logo', models.ImageField(upload_to='footer_logo')),
                ('link_url_1', models.CharField(max_length=200)),
                ('text_1', models.CharField(max_length=200)),
                ('link_url_2', models.CharField(max_length=200)),
                ('text_2', models.CharField(max_length=200)),
                ('link_url_3', models.CharField(max_length=200)),
                ('text_3', models.CharField(max_length=200)),
                ('link_url_4', models.CharField(max_length=200)),
                ('text_4', models.CharField(max_length=200)),
                ('link_url_5', models.CharField(max_length=200)),
                ('text_5', models.CharField(max_length=200)),
                ('link_url_6', models.CharField(max_length=200)),
                ('text_6', models.CharField(max_length=200)),
                ('link_url_7', models.CharField(max_length=200)),
                ('text_7', models.CharField(max_length=200)),
                ('link_url_8', models.CharField(max_length=200)),
                ('text_8', models.CharField(max_length=200)),
                ('link_url_9', models.CharField(max_length=200)),
                ('text_9', models.CharField(max_length=200)),
                ('logo_facebook', models.ImageField(upload_to='footer_logo')),
                ('text_facebook', models.CharField(max_length=200)),
                ('logo_twitter', models.ImageField(upload_to='footer_logo')),
                ('text_twitter', models.CharField(max_length=200)),
                ('logo_weibo', models.ImageField(upload_to='footer_logo')),
                ('text_weibo', models.CharField(max_length=200)),
                ('cpright_field', models.TextField()),
            ],
            options={
                'verbose_name': 'Footer',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Galary',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='photoblog_plugins_galary', to='cms.CMSPlugin', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='galary')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Galary',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Image_Link_New',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='photoblog_plugins_image_link_new', to='cms.CMSPlugin', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image_link')),
                ('text', models.CharField(max_length=200)),
                ('link_url', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Image Link',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='My_Pictures',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='photoblog_plugins_my_pictures', to='cms.CMSPlugin', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
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
