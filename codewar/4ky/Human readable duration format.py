def format_duration(seconds):
    if seconds==0:
        return "now"
    year = seconds // 31536000
    yearDay = seconds % 31536000
    day = yearDay // 86400
    dayHour = yearDay % 86400
    hour = dayHour // 3600
    hourMinute = dayHour % 3600
    minute = hourMinute // 60
    second = hourMinute % 60
    res = [year, day, hour, minute, second]
    res[0] = yearInput(res[0])
    res[1] = dayInput(res[1])
    res[2] = hourInput(res[2])
    res[3] = minuteInput(res[3])
    res[4] = secondInput(res[4])
    res = [i for i in res if i != ""]
    if len(res) >= 2:
        res[-2] = res[-2][:-1]+" and"
    res[-1]=res[-1][0:-1]    
    return " ".join(res)


def secondInput(s):
    if s == 0:
        return ""
    elif s == 1:
        return "1 second,"
    else:
        return f"{s} seconds,"


def minuteInput(m):
    if m == 0:
        return ""
    elif m == 1:
        return "1 minute,"
    else:
        return f"{m} minutes,"


def hourInput(h):
    if h == 0:
        return ""
    elif h == 1:
        return "1 hour,"
    else:
        return f"{h} hours,"


def dayInput(d):
    if d == 0:
        return ""
    elif d == 1:
        return "1 day,"
    else:
        return f"{d} days,"


def yearInput(y):
    if y == 0:
        return ""
    elif y == 1:
        return "1 year,"
    else:
        return f"{y} years,"