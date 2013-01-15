# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_social.models import Like, Mail


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
            'fields': ('title', 'description', 'image',)
        }),
    )

plugin_pool.register_plugin(LikePlugin)


class MailPlugin(CMSPluginBase):
    model = Mail
    name = _('Mail Plugin')
    render_template = 'djangocms_social/plugins/mail.html'

    module = 'Social'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['subject'] = instance.subject.replace(' ', '%20')
        context['body'] = instance.body.replace(' ', '%20')
        return context

plugin_pool.register_plugin(MailPlugin)