#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n):
    if n <= 1:
        return 0  # Base case: If n is 0 or 1, no operations needed

    operations = [0] * (n + 1)  # array to store the minimum operations
    for i in range(2, n + 1):
        operations[i] = float('inf')  # Initialize each value with infinity

        # Try all possible factors j of i
        for j in range(1, i):
            if i % j == 0:

                operations[i] = min(operations[i], operations[j] + (i // j))

    return operations[n]  # Return the minimum operations for n
