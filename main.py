#!/usr/bin/env python3

from handler import Handler
from label import label
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

  print("Blocks")
  for block in blocks:
    block.debug()
  print("Chars")
  for char in chars:
    char.debug()
  print("Emojis")
  for emoji in emojis:
    emoji.debug()
  print("Groups")
  for group in groups:
    group.debug()

  print("blocks: %d, chars: %d, emojis: %d, sum: %d" % (
    len(blocks),
    len(chars),
    len(emojis),
    len(emojis) + len(chars)
  ))


if __name__ == '__main__':
  run()
