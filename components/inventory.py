libtcod_dir = "/dev/libtcod-1.7.0-x86_64-msvc/"

import sys
sys.path.append(libtcod_dir + 'python/')

import libtcodpy as libtcod

from game_messages import Message


class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_items(self, item):
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                'item_added': None,
                'message': Message('You cannot carry any more, your inventory is full',
                                   libcotd.yellow)
            })
        else:
            results.append({
                'item_added': item,
                'message': Message('You pick up the {0}!'.format(item.name), libcotd.blue)
            })

            self.items.append(item)

        return results
