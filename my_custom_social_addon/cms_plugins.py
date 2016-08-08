# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class SocialPlugin(CMSPluginBase):
    model = models.Social
    name = 'Social Plugin'
    render_template = 'my_custom_social_addon/social.html'
    allow_children = True
    child_classes = ['SocialIconPlugin']


class SocialIconPlugin(CMSPluginBase):
    model = models.SocialIcon
    name = 'Icon'
    render_template = 'my_custom_social_addon/icon.html'
    require_parent = True
    parent_classes = ['SocialPlugin']


plugin_pool.register_plugin(SocialPlugin)
plugin_pool.register_plugin(SocialIconPlugin)
