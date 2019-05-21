import math


def binary_array_to_number(arr):
    arr_len = len(arr)
    res = 0
    for i in range(arr_len):
        res += arr[i]*math.pow(2, len(arr)-1-i)
    return res
