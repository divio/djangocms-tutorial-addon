# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, related_name='my_custom_social_addon_social', auto_created=True, to='cms.CMSPlugin', primary_key=True)),
                ('label', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SocialIcon',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, related_name='my_custom_social_addon_socialicon', auto_created=True, to='cms.CMSPlugin', primary_key=True)),
                ('url_link', models.URLField()),
                ('link_title', models.CharField(max_length=200, blank=True)),
                ('extra_classes', models.CharField(max_length=200, blank=True)),
                ('icon', models.ForeignKey(to='my_custom_social_addon.Icon')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
