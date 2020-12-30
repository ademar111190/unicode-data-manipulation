#!/usr/bin/env python3

from xml.sax import ContentHandler
from data import Block, Char, Emoji


TAG_ANNOTATION = "annotation"
TAG_BLOCK = "block"
TAG_CHAR = "char"
TAG_EMOJI = "emoji-source"
CODE_POINT = "cp"


class Handler(ContentHandler):

  def __init__(self):
    super(Handler, self).__init__()
    self.current_tag = None
    self.current_annotated = None
    self.chars = []
    self.current_char = None
    self.blocks = []
    self.current_block = None
    self.emojis = []
    self.current_emoji = None
    self.code_point_map = {}

  def startElement(self, tag, attrs):
    self.current_tag = tag
    if tag == TAG_ANNOTATION:
      if CODE_POINT in attrs:
        code_point = attrs[CODE_POINT]
        if len(code_point) == 1:
          code_point = '%04x' % ord(code_point)
        else:
          code_point = " ".join(['%04x' % ord(c) for c in code_point])
        code_point = code_point.upper()
        if code_point in self.code_point_map:
          self.current_annotated = self.code_point_map[code_point]
          self.current_annotated.populate_annotation(code_point, attrs)
        else:
          self.current_emoji = Emoji()
          self.current_emoji.populate_annotation(code_point, attrs)
          self.emojis.append(self.current_emoji)
          self.code_point_map[self.current_emoji.unicode] = self.current_emoji
          self.current_annotated = self.current_emoji

    elif tag == TAG_BLOCK:
      self.current_block = Block()
      self.current_block.populate(attrs)
      self.blocks.append(self.current_block)

    elif tag == TAG_CHAR:
      self.current_char = Char()
      self.current_char.populate(attrs)
      self.chars.append(self.current_char)
      self.code_point_map[self.current_char.single_code_point] = self.current_char

    elif tag == TAG_EMOJI:
      self.current_emoji = Emoji()
      self.current_emoji.populate(attrs)
      self.emojis.append(self.current_emoji)
      self.code_point_map[self.current_emoji.unicode] = self.current_emoji

  def endElement(self, tag):
    self.current_tag = None
    if tag == TAG_ANNOTATION:
      self.current_annotated = None

  def characters(self, content):
    if self.current_tag == TAG_ANNOTATION and self.current_annotated != None:
      self.current_annotated.populate_annotation_characters(content)

