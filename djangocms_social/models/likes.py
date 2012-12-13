# -*- coding: utf-8 -*-
from djangocms_social.models.base import RenderObject


AVAILABLE = {
    'facebook': 'FacebookLike',
    'google': 'GooglePlusOne',
}


class FacebookLike(RenderObject):
    template = 'djangocms_social/plugins/likes/facebook.html'

class GooglePlusOne(RenderObject):
    template = 'djangocms_social/plugins/likes/google.html'