#!/usr/bin/env python

import argparse

from json2html import Json2Html

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='file', type=argparse.FileType('r'), help="source json file")
    args = parser.parse_args()
    jh = Json2Html()
    jh.load_json_from_file(args.file)
    print(jh.output_task3())
