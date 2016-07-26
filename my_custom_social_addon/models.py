# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin


@python_2_unicode_compatible
class Social(CMSPlugin):
    label = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Icon(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class SocialIcon(CMSPlugin):
    icon = models.ForeignKey(Icon)
    url_link = models.URLField()
    link_title = models.CharField(
        blank=True,
        max_length=200,
    )
    extra_classes = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.link_title or self.url_link

    def copy_relations(self, oldinstance):
        # Because we have a ForeignKey (icon), it's required to copy over
        # the reference to the Icon instance to the new plugin.
        self.icon = oldinstance.icon
