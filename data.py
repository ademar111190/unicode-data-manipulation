#!/usr/bin/env python3

from ast import literal_eval


FIRST_CODE_POINT = "first-cp"
LAST_CODE_POINT = "last-cp"
SINGLE_CODE_POINT = "cp"
NAMES = ["na", "na1", "name"]


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
      literal_eval("".join(["\"\\u" + c + "\"" for c in self.single_code_point.split(" ")])) + \
      "\";\"" + \
      self.name + \
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
