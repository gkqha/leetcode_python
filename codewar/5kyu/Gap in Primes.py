from math import sqrt


def gap(g, m, n):
    primes = [0, 0]
    for i in range(m, n+1):
        if isPrimes(i):
            if primes[0] == 0:
                primes[0] = i
            elif primes[1] == 0:
                primes[1] = i
            else:
                primes[0], primes[1] = primes[1], i
        if primes[1]-primes[0] == g:
            return primes
    return None


def isPrimes(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
