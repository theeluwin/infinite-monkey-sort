#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


def infinite_monkey_sort(numbers):
    length = len(str(numbers))
    while True:
        monkey_output = ''.join([chr(int(random.random() * 255)) for i in range(length)])
        if monkey_output[0] != '[' or monkey_output[-1] != ']':
            continue
        if len([comma for comma in monkey_output if comma == ',']) != len(numbers) - 1:
            continue
        monkey_array = monkey_output[1:-1].replace(' ', '').split(',')
        if len([digit for digit in monkey_array if digit.isdigit()]) != len(monkey_array):
            continue
        monkey_array = [int(digit) for digit in monkey_array]
        sorted = True
        for index in range(1, len(monkey_array)):
            if monkey_array[index - 1] > monkey_array[index]:
                sorted = False
                break
        if sorted:
            return monkey_array
