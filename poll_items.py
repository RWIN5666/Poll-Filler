#!/usr/bin/env python3


class Poll_Item:
    def __init__(self, name, image_link):
        self.name = name
        self.image_link = image_link


def create_item_list(items_file_path):
    items_file = open(items_file_path, "r")
    if items_file.mode == "r":
        items_list = []
        items_lines = items_file.readlines()
        for elt_line in items_lines:
            print(elt_line)
            # first word is item's name
            # second word between parenthesis is the link
            # between brackets the number of times the item has been chosen in previous polls
            item_name = elt_line[: elt_line.find("(")]
            item_link = elt_line[elt_line.find("(") + 1 : elt_line.find(")")]
            print(f"item link {item_link} and item name {item_name}")
            new_item = Poll_Item(item_name, item_link)
            items_list.append(new_item)
        return items_list
