def create_register(num):
    num = int(num)
    keepnum = ""
    for i in range(3):
        if ((num >> i) & 001 == 1):
            keepnum += '1';
        else:
            keepnum += '0';
    return keepnum[::-1]


def create_machine(case, num1, num2, num3):
    if case == "add":

        opcode = "000"

    elif case == "nand":

        opcode = "001"

    othernum = "0000000000000"
    alll = opcode + " " + num2 + " " + num1 + " " + othernum + " " + num3
    return alll


def run_R_type(R_type):
    name = R_type
    keep_type = ""
    num1 = ""
    num2 = ""
    num3 = ""
    num = name.find(' ')

    firstnum1 = name.find('x')
    lastnum1 = name.find(',')
    keep1 = firstnum1
    firstnum2 = name.find('x', firstnum1 + 1)
    lastnum2 = name.find(',', lastnum1 + 1)
    keep2 = firstnum2
    firstnum3 = name.find('x', firstnum2 + 1)
    lastnum3 = len(name)
    keep3 = firstnum3

    for i in range(num):
        keep_type = keep_type + name[i]

    for i in range((lastnum1 - firstnum1) - 1):
        num1 += name[keep1 + 1]
        keep1 = keep1 + 1

    for i in range((lastnum2 - firstnum2) - 1):
        num2 += name[keep2 + 1]
        keep2 = keep2 + 1

    for i in range((lastnum3 - firstnum3) - 1):
        num3 += name[keep3 + 1]
        keep3 += 1

    print(keep_type + ' ' + num1 + ' ' + num2 + ' ' + num3 + ' ')
    num3 = str(create_register(num3))
    num2 = str(create_register(num2))
    num1 = str(create_register(num1))

    print(create_machine(keep_type, num1, num2, num3))


run_R_type("add x1,x2,x3")