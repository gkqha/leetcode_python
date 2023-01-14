import math


def solution(a):
    if len(a) == 1:
        return a[0]

    def multi_gcd(array):
        l = len(array)
        if l == 1:
            return array[0]
        elif l == 2:
            return math.gcd(array[0], array[1])
        else:
            return math.gcd(multi_gcd(array[: l // 2]), multi_gcd(array[l // 2 :]))

    return int(multi_gcd(a)) * len(a)