#!/usr/bin/env python3

import re
from data import Char, Emoji, emoji


CURRENT_GROUP_ID = 1
CURRENT_SUB_GROUP_ID = 1


def label(handler):
  groups = []
  group = None
  sub_group = None
  with open("emoji.txt", "r") as reader:
    line = reader.readline()
    while line != '':
      line = line.strip()
      if len(line) > 0:
        if line.startswith("#"):
          if line.startswith("# group:"):
            group = Group(line.split("# group:")[1].strip())
            groups.append(group)
          elif line.startswith("# subgroup:"):
            sg_name = line.split("# subgroup:")[1].strip().replace("-", " ").title()
            sub_group = SubGroup(sg_name)
            group.subgroups.append(sub_group)
        else:
          code_point = line[0:55].strip().upper()
          if code_point in handler.code_point_map:
            emoji = handler.code_point_map[code_point]
          else:
            emoji = Emoji()
            emoji.unicode = code_point
            handler.code_point_map[code_point] = emoji
          emoji.name["en"].add(re.compile("E\\d*\\.\\d*").split(line)[1].strip().title())
          sub_group.emojis.append(emoji)
      line = reader.readline()
  return groups


class Group(object):

  def __init__(self, name):
    super(Group, self).__init__()
    global CURRENT_GROUP_ID
    self.id = CURRENT_GROUP_ID
    CURRENT_GROUP_ID = CURRENT_GROUP_ID + 1
    self.name = name
    self.subgroups = []

  def debug(self):
    print("Group: %s" % (self.name))
    for sub_group in self.subgroups:
      print("\tSubGroup: %s" % (sub_group.name))
      for item in sub_group.emojis:
        if isinstance(item, Emoji):
          print("\t\tEmoji: \"%s\";\"%s\";\"%s\"" % (
            item.unicode,
            emoji(item.unicode),
            str(item.name)
          ))
        else:
          print("\t\tChar: \"%s\";\"%s\";\"%s\"" % (
            item.single_code_point,
            emoji(item.single_code_point),
            str(item.name)
          ))

class SubGroup(object):

  def __init__(self, name):
    super(SubGroup, self).__init__()
    global CURRENT_SUB_GROUP_ID
    self.id = CURRENT_SUB_GROUP_ID
    CURRENT_SUB_GROUP_ID = CURRENT_SUB_GROUP_ID + 1
    self.name = name
    self.emojis = []

