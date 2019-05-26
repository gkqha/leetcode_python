def tickets(people):
    tmp = 0
    for i in people:
        if i == 25:
            tmp += 25
        else:
            tmp -= i-25
    return "NO" if tmp < 0 else "YES"
