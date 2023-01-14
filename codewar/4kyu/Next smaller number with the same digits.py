def next_smaller(n):
    n_list = list(reversed([int(x) for x in str(n)]))
    for i in range(0, len(n_list) - 1):
        if n_list[i] < n_list[i + 1]:
            rest = sorted(n_list[0 : i + 1], reverse=True)
            print(rest, n_list[i + 1])
            for j in range(0, len(rest) + 1):
                if rest[j] < n_list[i + 1]:
                    if rest[j] == 0 and i + 1 == len(n_list)-1:
                        return -1
                    rest[j], n_list[i + 1] = n_list[i + 1], rest[j]
                    print(rest[j], n_list[i + 1])
                    break

            res = int(
                "".join(str(l) for l in list(reversed(sorted(rest) + n_list[i + 1 :])))
            )
            return res
    return -1


print(next_smaller(1027))
