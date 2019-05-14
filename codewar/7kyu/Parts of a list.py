def partlist(arr):
    res = []
    for i in range(len(arr)-1):
        head = ""
        for j in range(0, i+1):
            if j != i:
                head += arr[j]+" "
            else:
                head += arr[j]
        rest = ""
        for q in range(i+1, len(arr)):
            if q != len(arr)-1:
                rest += arr[q]+" "
            else:
                rest += arr[q]
        res.append((head, rest))
    return res
