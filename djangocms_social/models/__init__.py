# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from djangocms_social.utils import get_class
from djangocms_social.models import likes
from djangocms_social import defaults


class Like(CMSPlugin):
    facebook = models.BooleanField(_('facebook'), default=False)
    google = models.BooleanField(_('google'), default=False)

    # options
    title = models.CharField(_('title'), max_length=255, default=defaults.LIKE['title'], blank=True, null=True,
        help_text=_('Uses the title of the browser window if empty.'))
    description = models.CharField(_('description'), max_length=255, default=defaults.LIKE['description'],
        blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super(Like, self).__init__(*args, **kwargs)
        self.options = likes.AVAILABLE

    @property
    def get_objects(self):
        objects = []
        for type, object in self.options.iteritems():
            if getattr(self, type, False):
                objects.append(get_class(object)(**self.get_kwargs))
        return objects

    @property
    def get_kwargs(self):
        kwargs = {
            'title': self.title,
            'description': self.description,
        }
        return kwargs
