#!/usr/bin/env python3

from handler import Handler
from label import label
from sqlite import generate_sqlite
from xml.sax import make_parser
from xml.sax.handler import feature_namespaces


def parse():
  handler = Handler()
  parser = make_parser()
  parser.setFeature(feature_namespaces, 0)
  parser.setContentHandler(handler)
  for file in [
    "source.xml",
    "annotations_en.xml",
    "annotations_derived_en.xml"
  ]:
    parser.parse(file)
  return handler


def run():
  handler = parse()
  groups = label(handler)
  blocks = [block for block in handler.blocks if block.is_valid()]
  chars = [char for char in handler.chars if char.is_valid()]
  emojis = [emoji for emoji in handler.emojis if emoji.is_valid()]
  generate_sqlite(chars, emojis, blocks, groups)


if __name__ == '__main__':
  run()
