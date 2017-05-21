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
        j2h.load_json_from_file(open('sources/source.json'))
        self.assertEqual(str(j2h.output()),
                         '<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>'
                         )

    def test_task2(self):
        j2h = Json2Html()
        j2h.load_json_from_file(open('sources/source_task2.json'))
        self.assertEqual(str(j2h.output()),
                         '<h3>Title #1</h3><div>Hello, World 1!</div>'
                         )

    def test_task3(self):
        j2h = Json2Html()
        j2h.load_json_from_file(open('sources/source_task3.json'))
        self.assertEqual(str(j2h.output_task3()),
                         '<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>'
                         )

    def test_task4_1(self):
        j2h = Json2Html()
        j2h.load_json_from_file(open('sources/source_task4_1.json'))
        self.assertEqual(str(j2h.output_task3()),
                         '<ul><li><span>Title #1</span><content><ul><li><p>Example 1</p><header>header 1</header></li></ul></content></li><li><div>div 1</div></li></ul>'
                         )

    def test_task4_2(self):
        j2h = Json2Html()
        j2h.load_json_from_file(open('sources/source_task4_2.json'))
        self.assertEqual(str(j2h.output_task3()),
                         '<p>hello1</p>'
                         )


if __name__ == '__main__':
    unittest.main()
