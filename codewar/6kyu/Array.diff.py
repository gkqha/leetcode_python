def array_diff(a, b):
    res = []
    for tmp in a:
        if tmp not in b:
            res.append(tmp)
    return res