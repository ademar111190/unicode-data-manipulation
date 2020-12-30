#!/usr/bin/env python3

from xml.sax import ContentHandler
from data import Char


class Handler(ContentHandler):

  def __init__(self):
    super(Handler, self).__init__()
    self.chars = []
    self.current_char = None

  def startElement(self, tag, attrs):
    if tag == "char":
      self.current_char = Char()
      self.current_char.populate(attrs)

  def endElement(self, tag):
    if tag == "char" and self.current_char.is_valid():
      self.chars.append(self.current_char)
