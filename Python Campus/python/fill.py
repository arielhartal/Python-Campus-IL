def filter_teens(a=13, b=13, c=13):
    if (13 <= a <= 19) and (a != 15 and a != 16):
        fix_age(a)
    elif (13 <= b <= 19) and (b != 15 and b != 16):
        fix_age(b)
    elif (13 <= c <= 19) and (c != 15 and c != 16):
        fix_age(c)

    return a + b + c


def fix_age(age):
    age == 0
    return age


filter_teens(6, 9, 10)