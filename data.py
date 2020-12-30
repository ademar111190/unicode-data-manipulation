#!/usr/bin/env python3

from ast import literal_eval


FIRST_CODE_POINT = "first-cp"
LAST_CODE_POINT = "last-cp"
CODE_POINT = "cp"
UNICODE = "unicode"
NAMES = ["na", "na1", "name"]
NAME_ENGLISH = "en"


def emoji(code_point):
  codes = code_point.split(" ")
  fixed_codes = []
  for c in codes:
    size = len(c)
    if size == 4:
      fixed_codes.append("\"\\u" + c + "\"")
    elif size == 5:
      fixed_codes.append("\"\\U000" + c + "\"")
    elif size == 6:
      fixed_codes.append("\"\\U00" + c + "\"")
    elif size == 7:
      fixed_codes.append("\"\\U0" + c + "\"")
    elif size == 8:
      fixed_codes.append("\"\\U" + c + "\"")
  return literal_eval("".join(fixed_codes))


class Char(object):

  def __init__(self):
    super(Char, self).__init__()
    self.single_code_point = None
    self.name = {
      NAME_ENGLISH: set()
    }

  def populate(self, attrs):
    if CODE_POINT in attrs:
      self.single_code_point = attrs[CODE_POINT].upper()
    for name in NAMES:
      if name in attrs:
        self.name[NAME_ENGLISH].add(attrs[name].title())

  def populate_annotation(self, code_point, attrs):
    pass

  def populate_annotation_characters(self, content):
    for name in content.split(" | "):
      self.name[NAME_ENGLISH].add(name.title())

  def is_valid(self):
    return self.single_code_point != None

  def debug(self):
    print("\"%s\";\"%s\";\"%s\"" % (
      self.single_code_point,
      emoji(self.single_code_point),
      str(self.name)
    ))


class Emoji(object):

  def __init__(self):
    super(Emoji, self).__init__()
    self.unicode = None
    self.name = {
      NAME_ENGLISH: set()
    }

  def populate(self, attrs):
    if UNICODE in attrs:
      self.unicode = attrs[UNICODE].upper()

  def populate_annotation(self, code_point, attrs):
    if self.unicode == None:
      self.unicode = code_point

  def populate_annotation_characters(self, content):
    for name in content.split(" | "):
      if self.unicode == "1F52B" and "water" in name:
        continue
      self.name[NAME_ENGLISH].add(name.title())

  def is_valid(self):
    return self.unicode != None

  def debug(self):
    print("\"%s\";\"%s\";\"%s\"" % (
      self.unicode,
      emoji(self.unicode),
      str(self.name)
    ))


class Block(object):

  def __init__(self):
    super(Block, self).__init__()
    self.first_code_point = None
    self.last_code_point = None
    self.name = {
      NAME_ENGLISH: set()
    }

  def populate(self, attrs):
    if FIRST_CODE_POINT in attrs:
      self.first_code_point = attrs[FIRST_CODE_POINT]
    if LAST_CODE_POINT in attrs:
      self.last_code_point = attrs[LAST_CODE_POINT]
    for name in NAMES:
      if name in attrs:
        self.name[NAME_ENGLISH].add(attrs[name].title())

  def is_valid(self):
    return self.first_code_point != None and self.last_code_point != None

  def debug(self):
    print("\"%s\";\"%s\";\"%s\"" % (
      self.first_code_point,
      self.last_code_point,
      str(self.name)
    ))
