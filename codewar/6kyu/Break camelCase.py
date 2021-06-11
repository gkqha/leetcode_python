def solution(s):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for i in s:
        if i in abc:
            res = res + " "+i
        else:
            res += i
    if res[0] == " ":
        return res[-1]
    return res
