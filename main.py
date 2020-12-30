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
  return handler.chars


def run():
  chars = []
  print(">> " + str(len(chars)))
  chars.extend(parse_file("ucd.all.grouped.xml"))
  print(">> " + str(len(chars)))
  chars.extend(parse_file("ucd.nounihan.grouped.xml"))
  print(">> " + str(len(chars)))
  chars.extend(parse_file("ucd.unihan.grouped.xml"))
  print(">> " + str(len(chars)))
  for char in chars:
    char.print_single_point()


if __name__ == '__main__':
  run()
