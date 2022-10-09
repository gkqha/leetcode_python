def encode_rail_fence_cipher(string, n):
    if string == "":
        return ""
    rail = [["" for i in range(len(string))] for j in range(n)]
    dir, row, col = False, 0, 0
    for i in range(len(string)):
        if i % (n - 1) == 0:
            dir = not dir
        rail[row][col] = string[i]
        if dir == True:
            row = row + 1
            col = col + 1
        else:
            row = row - 1
            col = col + 1
    result = ""

    for i in rail:
        result = result + "".join(i)
    return result


def decode_rail_fence_cipher(string, n):
    if string == "":
        return ""
    rail = [["" for i in range(len(string))] for j in range(n)]
    dir, row, col = False, 0, 0
    for i in range(len(string)):
        if i % (n - 1) == 0:
            dir = not dir
        rail[row][col] = True
        if dir == True:
            row = row + 1
            col = col + 1
        else:
            row = row - 1
            col = col + 1
    tmp = string
    for i in range(0, len(rail)):
        for j in range(0, len(rail[0])):
            print(i, j)
            if rail[i][j] == True:
                rail[i][j] = tmp[0]
                tmp = tmp[1:]
    result = ""
    for i in range(0, len(string)):
        for j in range(0, len(rail)):
            if rail[j][i] != "":
                result = result + rail[j][i]

    return result


print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))
