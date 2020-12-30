#!/usr/bin/env python3

from xml.sax import ContentHandler
from data import Block, Char, Emoji


TAG_CHAR = "char"
TAG_BLOCK = "block"
TAG_EMOJI = "emoji-source"


class Handler(ContentHandler):

  def __init__(self):
    super(Handler, self).__init__()
    self.chars = []
    self.current_char = None
    self.blocks = []
    self.current_block = None
    self.emojis = []
    self.current_emoji = None

  def startElement(self, tag, attrs):
    if tag == TAG_CHAR:
      self.current_char = Char()
      self.current_char.populate(attrs)
    elif tag == TAG_BLOCK:
      self.current_block = Block()
      self.current_block.populate(attrs)
    elif tag == TAG_EMOJI:
      self.current_emoji = Emoji()
      self.current_emoji.populate(attrs)

  def endElement(self, tag):
    if tag == TAG_CHAR and self.current_char.is_valid():
      self.chars.append(self.current_char)
    elif tag == TAG_BLOCK and self.current_block.is_valid():
      self.blocks.append(self.current_block)
    elif tag == TAG_EMOJI and self.current_emoji.is_valid():
      self.emojis.append(self.current_emoji)
