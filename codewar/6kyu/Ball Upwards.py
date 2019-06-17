def max_ball(v0):
    v00 = v0*1000/3600
    t = 1
    res = 0
    while True:
        tmp = height(v00, t/10)
        if res < tmp:
            res = tmp
            t += 1
        else:
            break
    return t-1


def height(v, t):
    return v*t-0.5*9.81*t*t
