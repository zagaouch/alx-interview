#!/usr/bin/python3
"""
Main file for testing
"""

import math


def minOperations(n):
    def gd(number):
        greatest_divisor = 1
        for i in range(2, number//2 + 1):
            if number % i == 0:
                greatest_divisor = i
        return greatest_divisor

    h = gd(n)
    p = gd(n)
    o = gd(n) + 1
    while h < n:
        h = h + p
        o = o + 1
    return o
