from math import isqrt
from typing import List


def sieve_of_erastothenes(limit: int) -> List[int]:
    if limit <= 2:
        return []

    is_prime = [True] * limit
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(limit) + 1):
        if is_prime[i]:
            for x in range(i**2, limit, i):
                is_prime[x] = False
    primes = [i for i in range(limit) if is_prime[i]]
    return primes
