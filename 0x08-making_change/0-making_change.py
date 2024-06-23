#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a value greater than
    # the possible number of coins needed
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Populate dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
