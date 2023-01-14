def multiplication_table(size):
    result = [[] for i in range(size)]
    for out in range(size):
        i = out + 1
        for s in range(size):
            result[out].append(i)
            i += out + 1
    print(result)


multiplication_table(3)
