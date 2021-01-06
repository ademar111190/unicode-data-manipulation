#!/usr/bin/env python3

from os import remove
from sqlite3 import connect
from textwrap import dedent
from data import Char


NAME_ENGLISH = "en"


def generate_sqlite(chars, emojis, blocks, groups):
  sqlite_file = "unicode.sqlite"
  remove(sqlite_file)
  conn = connect(sqlite_file)
  cursor = conn.cursor()
  for create_query in [

    """
      CREATE TABLE chars (
        code TEXT PRIMARY KEY NOT NULL
      );
    """,

    """
      CREATE TABLE blocks (
        id INTEGER PRIMARY KEY NOT NULL
      );
    """,

    """
      CREATE TABLE groups (
        id INTEGER PRIMARY KEY NOT NULL
      );
    """,

    """
      CREATE TABLE sub_groups (
        id INTEGER PRIMARY KEY NOT NULL,
        group_id INTEGER NOT NULL
      );
    """,

    """
      CREATE TABLE char_block (
        char_code TEXT NOT NULL,
        block_id INTEGER NOT NULL
      );
    """,

    """
      CREATE TABLE char_sub_group (
        char_code TEXT NOT NULL,
        sub_group_id INTEGER NOT NULL
      );
    """,

    """
      CREATE TABLE char_name_en (
        char_code TEXT NOT NULL,
        name TEXT NOT NULL
      );
    """,

    """
      CREATE TABLE block_name_en (
        block_id INTEGER NOT NULL,
        name TEXT NOT NULL
      );
    """,

    """
      CREATE TABLE group_name_en (
        group_id INTEGER NOT NULL,
        name TEXT NOT NULL
      );
    """,

    """
      CREATE TABLE sub_group_name_en (
        sub_group_id INTEGER NOT NULL,
        name TEXT NOT NULL
      );
    """

  ]:
    cursor.execute(create_query)

  for char in chars:
    cursor.execute("""INSERT INTO chars VALUES ("{code}");""".format(
      code = char.single_code_point
    ))
    for name in char.name[NAME_ENGLISH]:
      cursor.execute("""INSERT INTO char_name_en VALUES ("{char_code}", "{name}");""".format(
        char_code = char.single_code_point,
        name = name
      ))
  conn.commit()

  for emoji in emojis:
    cursor.execute("""INSERT OR IGNORE INTO chars VALUES ("{code}");""".format(
      code = emoji.unicode
    ))
    for name in emoji.name[NAME_ENGLISH]:
      cursor.execute("""INSERT INTO char_name_en VALUES ("{char_code}", "{name}");""".format(
        char_code = emoji.unicode,
        name = name
      ))
  conn.commit()

  for block in blocks:
    cursor.execute("""INSERT INTO blocks VALUES ("{id}");""".format(
      id = block.id
    ))
    first = int(block.first_code_point, 16)
    last = int(block.last_code_point, 16) + 1
    for i in range(first, last):
      cursor.execute("""INSERT INTO char_block VALUES ("{char_code}", "{block_id}");""".format(
        char_code = "{:0>4X}".format(i),
        block_id = block.id
      ))
    for name in block.name[NAME_ENGLISH]:
      cursor.execute("""INSERT INTO block_name_en VALUES ("{block_id}", "{name}");""".format(
        block_id = block.id,
        name = name
      ))
  conn.commit()

  for group in groups:
    cursor.execute("""INSERT INTO groups VALUES ("{id}");""".format(
      id = group.id
    ))
    cursor.execute("""INSERT INTO group_name_en VALUES ("{group_id}", "{name}");""".format(
      group_id = group.id,
      name = group.name
    ))
    for sub_group in group.subgroups:
      cursor.execute("""INSERT INTO sub_groups VALUES ("{id}", "{group_id}");""".format(
        id = sub_group.id,
        group_id = group.id
      ))
      cursor.execute("""INSERT INTO sub_group_name_en VALUES ("{sub_group_id}", "{name}");""".format(
        sub_group_id = sub_group.id,
        name = sub_group.name
      ))
      for emoji in sub_group.emojis:
        if isinstance(emoji, Char):
          cursor.execute("""INSERT INTO char_sub_group VALUES ("{char_code}", "{sub_group_id}");""".format(
            char_code = emoji.single_code_point,
            sub_group_id = sub_group.id
          ))
        else:
          cursor.execute("""INSERT INTO char_sub_group VALUES ("{char_code}", "{sub_group_id}");""".format(
            char_code = emoji.unicode,
            sub_group_id = sub_group.id
          ))
  conn.commit()

  conn.execute("VACUUM")
  conn.commit()
  conn.close()
