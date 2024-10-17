#!/usr/bin/python3
"""
try_this_prime_game
"""


def isWinner(x, nums):
    """
    Returns the name of the player that won the most rounds
    """

    if x < 1:
        return None

    if len(nums) < x:
        return None

    primes = [2]

    for i in range(3, 10001):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    ben = 0
    maria = 0

    dp = [0] * (max(nums) + 1)
    at = 0
    for i in range(1, len(dp)):
        dp[i] = dp[i - 1]
        if at < len(primes) and primes[at] <= i:
            dp[i] += 1
            at += 1

    for n in nums:
        if dp[n] % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None