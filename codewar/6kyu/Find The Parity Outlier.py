def find_outlier(integers):
    d = list(map(lambda x: x % 2 == 0, integers))
    if d.count(True) == 1:
        return integers[d.index(True)]
    else:
        return integers[d.index(False)]
