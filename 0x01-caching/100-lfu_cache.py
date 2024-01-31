#!/usr/bin/env python3
"""
A class LFUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    '''
    This defines LFUCache
    '''

    def __init__(self):
        '''
        This initializes LFUCache
        '''
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        '''
        This assigns the item to the dictionary
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                least_freq_keys = [k for k, v in self.frequency.items()
                                   if v == min(self.frequency.values())]
                if len(least_freq_keys) == 1:
                    discarded_key = least_freq_keys[0]
                else:
                    discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                print(f'DISCARD: {discarded_key}')

            self.cache_data[key] = item
            self.order = [k for k in self.order if k != key] + [key]
            # Update the frequency of the current key
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        '''
        This returns the value associated with the given key
        '''
        if key is not None:
            if key in self.cache_data:
                self.order = [k for k in self.order if k != key] + [key]
                # Update the frequency of the current key
                self.frequency[key] += 1
                return self.cache_data[key]
        return None

    def update_lfu_queue(self, key):
        '''
        This updates LFU queue based on LFU frequencies
        '''
        self.queue.sort(key=lambda k: (self.frequency[k], k))
