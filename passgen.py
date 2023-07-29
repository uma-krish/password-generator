def generatepwd1(size):
    import random
    import string

    passwd = ""
    result = ""

    upper1 = list(string.ascii_uppercase)
    lower1 = list(string.ascii_lowercase)
    number1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list1 = upper1 + lower1 + number1

    len1 = len(upper1)
    len2 = len(lower1)
    len3 = len(number1)
    len4 = len(list1)

    position1 = random.randint(0, len1 - 1)
    position2 = random.randint(0, len2 - 1)
    position3 = random.randint(0, len3 - 1)

    passwd = passwd + upper1[position1] + lower1[position2] + number1[position3]

    for i in range(0, size - 3, 1):
        position4 = random.randint(0, len4 - 1)
        passwd = passwd + list1[position4]

    l = list(passwd)
    random.shuffle(l)
    result = "".join(l)

    return result


def generatepwd2(size, quantity):
    res = []
    for i in range(0, quantity, 1):
        a = generatepwd1(size)
        res.append(a)
    return res
