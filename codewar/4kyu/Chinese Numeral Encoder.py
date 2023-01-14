def to_chinese_numeral(n):
    numerals = {
        "-": "负",
        ".": "点",
        0: "零",
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九",
    }

    if n == 0:
        return "零"
    unit = {1: "", 2: "十", 3: "百", 4: "千", 5: "万"}
    res = ""
    n_list = list(map(str, str(n)))
    if n_list[0] == "-":
        res = "负"
        n_list = n_list[1:]
    if "." in n_list:
        dian_pos = n_list.index(".")
        for i in range(0, dian_pos):
            res = (
                res
                + (
                    ""
                    if (i != 0 and dian_pos - i != 0)
                    and (
                        (n_list[i + 1] == "0" or n_list[i + 1] == ".")
                        and n_list[i] == "0"
                    )
                    or (n_list[i] == "1" and i == 0 and dian_pos - i == 2)
                    else numerals[int(n_list[i])]
                )
                + (unit[dian_pos - i] if n_list[i] != "0" else "")
            )
        res = res + "点"
        for i in range(dian_pos + 1, len(n_list)):
            res = res + numerals[int(n_list[i])]
    else:
        for i in range(0, len(n_list)):
            res = (
                res
                + (
                    ""
                    if (
                        n_list[i] == "0"
                        and (i == len(n_list) - 1 or n_list[i + 1] == "0")
                    )
                    or (n_list[i] == "1" and i == 0 and len(n_list) == 2)
                    else numerals[int(n_list[i])]
                )
                + (unit[len(n_list) - i] if n_list[i] != "0" else "")
            )
    return res


print(to_chinese_numeral(10))
print(to_chinese_numeral(-14.1))
print(to_chinese_numeral(10006.005))
print(to_chinese_numeral(10010))
print(to_chinese_numeral(0.1))
