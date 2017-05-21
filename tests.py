#!/usr/bin/env python

import unittest

from html_tag import (P, H1)
from json2html import Json2Html


class TestModules(unittest.TestCase):

    def test_p(self):
        self.assertEqual(str(P('test')), '<p>test</p>')

    def test_h1(self):
        self.assertEqual(str(H1('test2')), '<h1>test2</h1>')

    def test_task1(self):
        j2h = Json2Html()
        j2h.load_json_from_file(open('source.json'))
        self.assertEqual(str(j2h.output()),
                         '<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>'
                         )


if __name__ == '__main__':
    unittest.main()
