#!/usr/bin/env python3

from handler import Handler
from xml.sax import make_parser
from xml.sax.handler import feature_namespaces


def parse_file(file):
  handler = Handler()
  parser = make_parser()
  parser.setFeature(feature_namespaces, 0)
  parser.setContentHandler(handler)
  parser.parse(file)
  return handler


def run():
  handler =  parse_file("source.xml")
  blocks = handler.blocks
  chars = handler.chars
  emojis = handler.emojis

  print("Blocks")
  for block in blocks:
    block.debug()
  print("Chars")
  for char in chars:
    char.debug()
  print("Emojis")
  for emoji in emojis:
    emoji.debug()

  print(
    "blocks: " + str(len(blocks)) + \
    ", chars: " + str(len(chars)) + \
    ", emojis: " + str(len(emojis)) + \
    ", sum: " + str(len(emojis) + len(chars)))


if __name__ == '__main__':
  run()
