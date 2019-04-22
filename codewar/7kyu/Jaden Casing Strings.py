def toJadenCase(string):
    # ...
    start = 0
    res = ""
    for end in range(len(string)):
        if string[end] == " " or end == len(string) - 1:
            res += (string[start].upper() + string[start + 1:end + 1])
            start = end + 1
    return print(res)


toJadenCase("How can mirrors be real if our eyes aren't real")
