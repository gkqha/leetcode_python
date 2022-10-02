def structure(l):
    res = []

    def cal(l):
        if isinstance(l,list):
            res.append(1)
            for i in l:
                cal(i)
        else:
            res.append(0)
        return res

    return cal(l)


def same_structure_as(original, other):
    return structure(original) == structure(other)


print(same_structure_as([],1))
