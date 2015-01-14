#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import unittest

from infinite_monkey_sort import infinite_monkey_sort


class TestSorted(unittest.TestCase):

    def setUp(self):
        self.numbers = range(4)
        random.shuffle(self.numbers)

    def test_sorted(self):
        self.assertEqual(infinite_monkey_sort(self.numbers), [0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
