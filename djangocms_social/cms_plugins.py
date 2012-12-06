# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_social.models import Like


class LikePlugin(CMSPluginBase):
    model = Like
    name = _('Like Plugin')
    render_template = 'djangocms_social/plugins/like.html'

    module = 'Social'

    fieldsets = (
        (None, {
            'fields': (('facebook', 'google',),)
        }),
        (_('Advanced'), {
            'fields': ('title', 'description',)
        })
    )

    def render(self, context, instance, placeholder):
        context['objects'] = instance.get_objects
        return context

plugin_pool.register_plugin(LikePlugin)