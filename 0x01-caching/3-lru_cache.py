#!/usr/bin/env python3
"""
A class LRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    This defines LRUCache
    '''

    def __init__(self):
        '''
        This initialize LRUCache
        '''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''
        This assigns the item to the dictionary
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # LRU eviction: Discard the least recently used item
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

            self.cache_data[key] = item
            self.order.append(key)
            self.order = [k for k in self.order if k != key] + [key]

    def get(self, key):
        '''
        This returns the value associated with the given key
        '''
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
