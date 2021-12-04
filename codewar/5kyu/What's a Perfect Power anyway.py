import math


def isPP(n):
    m = 1
    result = 0
    limit = math.sqrt(n)
    while m < limit:
        k = 1
        m = m + 1
        while result < n:
            result = m ** k
            print([m, k, result])
            if result == n:
                return [m, k]
            k = k + 1
        result = 0
    return None