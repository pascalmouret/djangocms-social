# -*- coding: utf-8 -*-
from django.template import Context
from django.template.loader import get_template


class RenderObject(object):
    template = None

    def __init__(self, *args, **kwargs):
        super(RenderObject, self).__init__()
        self.kwargs = kwargs

    def render(self):
        if not self.template:
            raise Exception('No template defined.')
        t = get_template(self.template)
        return t.render(Context(self.kwargs))