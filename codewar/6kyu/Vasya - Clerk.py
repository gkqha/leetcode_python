def tickets(people):
    tmp = {"25": 0, "50": 0}
    for i in people:
        if i == 25:
            tmp["25"] += 1
        else:
            if i == 50:
                tmp["50"] += 1
                tmp["25"] -= 1
            else:
                if tmp["50"] > 0:
                    tmp["50"] -= 1
                    tmp["25"] -= 1
                else:
                    tmp["25"] -= 3
        if tmp["25"] < 0:
            return "NO"
    return "YES"
