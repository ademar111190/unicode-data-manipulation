#!/usr/bin/env python3

from ast import literal_eval


FIRST_CODE_POINT = "first-cp"
LAST_CODE_POINT = "last-cp"
SINGLE_CODE_POINT = "cp"
UNICODE = "unicode"
NAMES = ["na", "na1", "name"]


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
    self.name = None

  def populate(self, attrs):
    if SINGLE_CODE_POINT in attrs:
      self.single_code_point = attrs[SINGLE_CODE_POINT]
    for name in NAMES:
      if name in attrs:
        self.name = attrs[name]
        break

  def is_valid(self):
    return self.single_code_point != None and self.name != None

  def debug(self):
    print("\"" + \
      self.single_code_point + \
      "\";\"" + \
      emoji(self.single_code_point) + \
      "\";\"" + \
      self.name + \
      "\"")


class Emoji(object):

  def __init__(self):
    super(Emoji, self).__init__()
    self.unicode = None

  def populate(self, attrs):
    if UNICODE in attrs:
      self.unicode = attrs[UNICODE]

  def is_valid(self):
    return self.unicode != None

  def debug(self):
    print("\"" + \
      self.unicode + \
      "\";\"" + \
      emoji(self.unicode) + \
      "\"")


class Block(object):

  def __init__(self):
    super(Block, self).__init__()
    self.first_code_point = None
    self.last_code_point = None
    self.name = None

  def populate(self, attrs):
    if FIRST_CODE_POINT in attrs:
      self.first_code_point = attrs[FIRST_CODE_POINT]
    if LAST_CODE_POINT in attrs:
      self.last_code_point = attrs[LAST_CODE_POINT]
    for name in NAMES:
      if name in attrs:
        self.name = attrs[name]
        break

  def is_valid(self):
    return self.first_code_point != None and self.last_code_point != None and self.name != None

  def debug(self):
    print("\"" + \
      self.first_code_point + \
      "\";\"" + \
      self.last_code_point + \
      "\";\"" + \
      self.name + \
      "\"")
