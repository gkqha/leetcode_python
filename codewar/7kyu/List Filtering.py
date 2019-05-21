def filter_list(l):
    'return a new list with the strings filtered out'

    def func(x):
        if type(x) == int:
            return True
        else:
            return x.isdigit()
    a = 1+1.0
    return list(filter(func(), l))
