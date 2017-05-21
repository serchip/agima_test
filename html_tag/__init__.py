# -*- coding: utf-8 -*-

import io


class Tag(object):
    """Generic class for tags"""
    tag = 'TXT'
    _CLOSING_TAG = ['H1', 'H2', 'H3', 'P', 'DIV', 'UL', 'LI']

    def __init__(self, *content, **attrs):
        self.attrs = attrs
        if not content:
            self.children = []
        elif isinstance(content[0], Tag) and content[0].__class__ is Tag:
            self.children = content[0].children
        else:
            self.children = [content[0]]

    def __str__(self):
        res = io.StringIO()
        w = res.write
        if type(self) != str:
            w(u"<%s>" % self.tag.lower())
        else:
            w(u'%s' % self)
        for child in self.children:
            w(u'%s' % str(child))
        if self.tag in self._CLOSING_TAG:
            w(u"</%s>" % self.tag.lower())
        return res.getvalue()


class P(Tag):
    tag = 'P'


class H1(Tag):
    tag = 'H1'


class H2(Tag):
    tag = 'H2'


class H3(Tag):
    tag = 'H3'


class DIV(Tag):
    tag = 'DIV'


class UL(Tag):
    tag = 'UL'


class LI(Tag):
    tag = 'LI'
