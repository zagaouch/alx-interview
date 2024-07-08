#!/usr/bin/python3
"""
They play x rounds of the game, where n may be different
for each round. Assuming Maria always goes first and both
kplayers play optimally, determine who the winner of each game is.
"""

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    
    # Sieve of Eratosthenes to find all prime numbers up to max_n
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_n + 1, i):
                primes[j] = False

    # Determine the winner for each possible n
    winner = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prime_count = 0
        for j in range(1, i + 1):
            if primes[j]:
                prime_count += 1
        # If prime_count is odd, Maria wins, otherwise Ben wins
        winner[i] = prime_count % 2
    
    maria_wins = 0
    ben_wins = 0

    # Count wins for each player based on precomputed results
    for n in nums:
        if winner[n] == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
