from Question1 import *
from Question2 import convert
from Question4 import find_min
import unittest

"""
TestAssignment to unit test all the scripts

@author: SP
"""


class TestAssignment(unittest.TestCase):
    def test_question1(self):
        """
        Test case for Question1
        :return: None
        """
        custom_list = CustomList()
        custom_list.append(1)
        self.assertEqual(custom_list._list, [1])

        custom_list.insert(1, 2)
        self.assertEqual(custom_list._list, [1, 2])

        custom_list.insert(4, 2)
        self.assertEqual(custom_list._list, [1, 2])

        custom_list.append(2)
        self.assertEqual(custom_list._list, [1, 2, 2])

        self.assertEqual(custom_list.unique_items(), [1, 2])

        self.assertEqual(custom_list.item_frequency(), {1: 1, 2: 2})

    def test_question2(self):
        """
        Test case for Question2
        :return: None
        """
        self.assertEqual(type(convert("1.0")), type(1.0))
        self.assertEqual(type(convert("1")), type(1))
        self.assertEqual(type(convert("121.sadas")), type(""))
        self.assertEqual(type(convert("sadasd")), type(""))

    def test_question4(self):
        """
        Test case for Question4
        :return: None
        """
        self.assertEqual(find_min(1, 2, 3), 1)
        self.assertEqual(find_min(-1, 1, 2), -1)
        self.assertEqual(find_min(5, 5, 5), 5)


if __name__ == '__main__':
    unittest.main()
