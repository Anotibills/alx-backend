#!/usr/bin/env python3
"""
Implement a method that takes the same arguments and returns a dictionary
"""
import csv
from math import ceil
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    '''
    This class serves to paginate a database of popular baby names.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''
        This initialize instance.
        '''
        self._dataset = None

    def _load_dataset(self) -> List[List[str]]:
        '''
        This cache the dataset.
        '''
        if self._dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                self._dataset = [row for row in reader][1:]

        return self._dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        '''
        This return a page of the dataset.
        '''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)

        return self.dataset()[start:end] if start < len(self.dataset()) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''
        This returns dictionary of pagination data.
        '''
        page_data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = ceil(total_data / page_size)

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': total_pages
        }
