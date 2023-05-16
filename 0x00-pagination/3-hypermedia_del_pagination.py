#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        This method takes with two integer arguments: index with a
        None default value and page_size with default value of 10
        and returns a dictionary with the necessarry index and necessary
        information
        """
        indexed_data_set = self.indexed_dataset()
        page_data = []
        i = 0
        current_index = index
        assert index < len(indexed_data_set)
        while i < page_size:
            data = indexed_data_set.get(index)
            if data is not None:
                page_data.append(data)
                i += 1
                index += 1
            else:
                index += 1
        next = index
        hyper_index = {
            'index': current_index,
            'data': page_data,
            'page_size': page_size,
            'next_index': next
        }

        return hyper_index
