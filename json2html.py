import json
from html_tag import (P, H1)
from collections import OrderedDict


class Json2Html(object):
    dict_store = {}

    def load_json_from_file(self, file):
        self.dict_store = json.load(file, object_pairs_hook=OrderedDict)

    def output(self):
        return self.dict_store

    def dict_to_html(self, dict_in):
        str_out = ''
        _keys_to_tag = {'body': P, 'title': H1}
        for key in dict_in.keys():
            if key in _keys_to_tag:
                str_out += str(_keys_to_tag[key](dict_in[key]))
        return str_out

    def list_to_dict(self, list_in):
        str_out_line = ''
        for line in list_in:
            if isinstance(line, dict):
                str_out_line += self.dict_to_html(line)
            else:
                str_out_line += self.list_to_dict(line)
        return str_out_line

    def output(self):
        return self.list_to_dict(self.dict_store)
