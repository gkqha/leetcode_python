def removNb(n):
    res = []
    sum = (1+n)*(n/2)
    for i in range(1, n+1):
        q = (sum - i)/(i+1)
        if q in range(i+1, n+1):
            res.append((i, q))
            res.append((q, i))
    return res
