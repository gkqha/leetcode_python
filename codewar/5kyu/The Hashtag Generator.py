def generate_hashtag(s):
    if len(s) > 140 or s == "":
        return False
    res = ["#"]+list(s)
    print(res)
    i = 0
    upper1 = False
    while i < len(res):
        if res[i] == " " or res[i] == "#":
            upper1 = True
        else:
            upper1 = False
            res[i] = res[i].lower()
        if i < len(res)-1 and upper1 == True and res[i+1] != " ":
            res[i+1] = res[i+1].upper()
            i += 1
        i += 1
    res = [x for x in res if x != " "]
    return "".join(res)


# def generate_hashtag(s):
#     output = "#"

#     for word in s.split():
#         output += word.capitalize()

#     return False if (len(s) == 0 or len(output) > 140) else output
