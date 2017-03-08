#!/usr/bin/env python

from collections import MutableSequence

"""
CustomList class which allows, append operation
and methods to return number of elements in the data structure
and frequency of elements in the structure

@author: SP
"""


class CustomList(MutableSequence):
    def __init__(self, data=None):
        """
        Initializer for the class
        :param data:
        """
        super(CustomList, self).__init__()
        self._list = []
        if data is not None:
            self._list = [i for i in data]

    def __getitem__(self, index):
        return self._list[index]

    def __delitem__(self, index):
        del self._list[index]

    def __len__(self):
        return len(self._list)

    def __setitem__(self, index, value):
        self._list[index] = value

    def append(self, item):
        """
        Method to append an element to the data structure
        :param item:
        :return: None
        """
        self.insert(len(self._list), item)

    def insert(self, position, new_item):
        """
        Method to insert an element in the data structure
        at a specified index
        :param new_item: element to be inserted
        :param position: index where to insert
        :return: None
        """
        if position > len(self._list):
            return OverflowError
        elif position == len(self._list):
            self._list.append(new_item)
        else:
            self._list[position] = new_item

    def unique_items(self):
        """
        Method to return all unique elements in the data structure
        :return: list of all unique elements
        """
        unique_items = self.item_frequency()
        return unique_items.keys()

    def item_frequency(self):
        """
        Method to return frequencies of elements in the data structure
        :return: dictionary
        """
        unique = {}
        for item in self:
            if item not in unique:
                unique[item] = 1
            else:
                unique[item] += 1
        return unique
