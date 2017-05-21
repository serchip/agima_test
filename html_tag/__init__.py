# -*- coding: utf-8 -*-

import io
import cgi


class Tag(object):
    """Generic class for tags"""
    tag = 'TXT'
    _CLOSING_TAG = ['H1', 'H2', 'H3', 'P', 'DIV', 'UL', 'LI', 'SPAN', "CONTENT", 'HEADER']

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
        w(u"<%s" % self.tag.lower())
        attr_list = []
        for k in self.attrs:
            value = self.attrs[k]
            if value:
                attr_list.append(' %s="%s"' % (k, ' '.join(value)))
        w(u"".join(attr_list))
        w(u">")
        for child in self.children:
            if isinstance(child, unicode):
                w(u'%s' % cgi.escape(child))
            else:
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


class SPAN(Tag):
    tag = 'SPAN'


class CONTENT(Tag):
    tag = 'CONTENT'


class HEADER(Tag):
    tag = 'HEADER'
