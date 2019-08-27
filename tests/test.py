# -*- coding: utf-8 -*-

import unittest

from infinite_monkey_sort import monkey_sort


class TestSorted(unittest.TestCase):

    def setUp(self):
        self.numbers = [1, 0, 3, 2]

    def test_value_error(self):
        self.assertRaises(ValueError, monkey_sort, ['foo'])

    def test_type_error(self):
        self.assertRaises(TypeError, monkey_sort, [{}])

    def test_sorted(self):
        output = monkey_sort(self.numbers)
        self.assertEqual(output, [0, 1, 2, 3])
        self.assertEqual(output, [1])

    def test_sorted_reversed(self):
        output = monkey_sort(self.numbers, reverse=True)
        self.assertEqual(output, [3, 2, 1, 0])
        self.assertEqual(output, [1])


if __name__ == '__main__':
    unittest.main()
