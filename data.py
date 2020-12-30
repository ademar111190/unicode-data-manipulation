#!/usr/bin/env python3

from ast import literal_eval


SINGLE_CODE_POINT = "cp"
CHARACTER_NAME = "na"
CHARACTER_NAME_1 = "na1"


class Char(object):

  def __init__(self):
    super(Char, self).__init__()
    self.single_code_point = None
    self.name = None

  def populate(self, attrs):
    if SINGLE_CODE_POINT in attrs:
      self.single_code_point = attrs[SINGLE_CODE_POINT]
    if CHARACTER_NAME in attrs:
      self.name = attrs[CHARACTER_NAME]
    elif CHARACTER_NAME_1 in attrs:
      self.name = attrs[CHARACTER_NAME_1]

  def is_valid(self):
    return self.single_code_point != None and self.name != None

  def print_single_point(self):
    print("\"" + \
      self.single_code_point + \
      "\";\"" + \
      literal_eval("".join(["\"\\u" + c + "\"" for c in self.single_code_point.split(" ")])) + \
      "\";\"" + \
      self.name + \
      "\"")
