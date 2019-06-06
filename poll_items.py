#!/usr/bin/env python3

import re

class Poll_Item:
    def __init__(self, name, image_link):
        self.name = name
        self.image_link = image_link


def create_item_list(items_file_path):
    """
    Parse a file to retrive items on it.
    Items must be formated as follow: name(link)
    """
    items_file = open(items_file_path, "r")
    pattern = re.compile(r'(.*)\((.*)\)')
    if items_file.mode == "r":
        items_list = []
        items_lines = items_file.readlines()
        for elt_line in items_lines:
            print(elt_line)
            # first word is item's name
            # second word between parenthesis is the link
            # between brackets the number of times the item has been chosen in previous polls
            m = pattern.match(elt_line)
            if None != m:
                item_name = m.group(1)
                item_link = m.group(2)
                print(f"item link {item_link} and item name {item_name}")
                new_item = Poll_Item(item_name, item_link)
                items_list.append(new_item)
            
        return items_list
