#!/usr/bin/env python3

from handler import Handler
from xml.sax import make_parser
from xml.sax.handler import feature_namespaces


def run():
  handler = Handler()
  parser = make_parser()
  parser.setFeature(feature_namespaces, 0)
  parser.setContentHandler(handler)
  for file in [
    "source.xml",
    "annotations_en.xml"
  ]:
    parser.parse(file)

  blocks = handler.blocks
  chars = handler.chars
  emojis = handler.emojis

  print("Blocks")
  for block in blocks:
    if block.is_valid():
      block.debug()
  print("Chars")
  for char in chars:
    if char.is_valid():
      char.debug()
  print("Emojis")
  for emoji in emojis:
    if emoji.is_valid():
      emoji.debug()

  print(
    "blocks: " + str(len(blocks)) + \
    ", chars: " + str(len(chars)) + \
    ", emojis: " + str(len(emojis)) + \
    ", sum: " + str(len(emojis) + len(chars)))


if __name__ == '__main__':
  run()
