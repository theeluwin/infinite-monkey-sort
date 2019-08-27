# -*- coding: utf-8 -*-

import random

from collections import Counter


def monkey_sort(numbers, reverse=False):

    # init
    numbers = [int(number) for number in numbers]  # should raise appropriate exception if numbers are not integers
    slen = len(','.join([str(number) for number in numbers]))
    n = len(numbers)

    # iteration
    while True:

        # create a monkey output
        result = ''.join([chr(int(random.random() * 255)) for i in range(slen)])

        # check if comma-separated values are integers
        values = result.split(',')
        if len(values) != n:
            continue
        flag = False
        for value in values:
            try:
                value = int(value)
            except ValueError:
                flag = True
                break
            except TypeError:
                flag = True
                break
        if flag:
            continue

        # check if elements match
        values = [int(value) for value in values]
        ci = Counter(numbers)
        co = Counter(values)
        if ci != co:
            continue

        # check if the numbers are sorted
        is_sorted = True
        for i in range(n - 1):
            if reverse:
                if values[i] <= values[i + 1]:
                    is_sorted = False
                    break
            else:
                if values[i] >= values[i + 1]:
                    is_sorted = False
                    break

        # if sorted, return
        if is_sorted:
            return values
