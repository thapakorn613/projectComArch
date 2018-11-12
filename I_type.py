
import reg as reg
import mem as mem
import convertTobinary as convert

def iType(message):
    messageSplit = message.split()
    print(messageSplit)
    # ----------------------------------------
    if messageSplit[1] == "lw":
        opcode = "010"
    elif messageSplit[1] == "sw":
        opcode = "011"
    elif messageSplit[1] == "beq":
        opcode = "100"
    else:
        opcode = "000"  # for check error
    # ----------------------------------------

    # ------------ create RS -----------------
    temprs = int(messageSplit[2])
    rs = convert.numToBinary(temprs, 3)
    # ----------------------------------------
    # ------------ create RS -----------------
    temprt = int(messageSplit[3])
    rt = convert.numToBinary(temprt, 3)
    # ----------------------------------------
    # ------------ create RS -----------------
    offsetField = ""
    if messageSplit[4] == mem.label:  # string other
        tempOffset = mem.addessPC
    else:
        tempOffset = messageSplit[4]
    int_Offset = int(tempOffset)
    offsetField = convert.numToBinary(int_Offset, 16)
    # ----------------------------------------
    # ------------ merge code to Machine Language --------
    machineCode = opcode + rs + rt + offsetField
    # ----------------------------------------------------
    print("opcode : " + opcode)
    print("rs : " + rs)
    print("rt : " + rt)
    print("offsetField : " + offsetField)
    #print("machineCode : " + machineCode)
    return machineCode

def numToBinary(n,rangeOffbit):
    result = ''
    for x in range(rangeOffbit):
        r = n % 2
        n = n // 2
        result += str(r)
    result = result[::-1]
    return result
