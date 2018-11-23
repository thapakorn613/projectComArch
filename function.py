def numToBinary(n,rangeOffbit):
    result = ''
    for x in range(rangeOffbit):
        r = n % 2
        n = n // 2
        result += str(r)
    result = result[::-1]
    return result



def binaryToDecimal(binary,rangeOfBit):
    if(binary[0:1]=="0"):
        #print(binary[0:1])
        return int(binary, 2)
    else:
        #print(binary[0:1])
        return  int(binary,2)-(1<<rangeOfBit);

# ---------------- Error check ------------------
# not complete all
def error_detect(mchcodee):
    listop = ['000','001','010','011','100','101','110','111']
    if len(mchcodee)!= 32:
        print('ERROR Machinecode out of bound!!!')
    elif mchcodee[7:10] not in listop: # opcode check
        print('ERROR Opcode not found!!!')
    elif mchcodee[0:7] != '0000000': # bit 25-31 is 0
        print('ERROR syntax error!!!!')
    else:
        print('Anything is pass!!!')

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def binToDecimal(str):
    n = 0
    temp = 0
    sum = 0
    str_exe = list (str)
    if(str[0:17] == '00000000000000001'):
        return CovertTwocomplement(str[16:32])
    else:
        for x in reversed(str_exe):
            if x == "1":
                temp = 2 ** n
            elif x == "0":
                temp = 0
            sum = sum + temp
            n = n + 1
        return sum


def CovertTwocomplement(_Codebit):
    Offset=0
    if(_Codebit[0]=='1'):
        Offset=int(_Codebit[0:16],2)-(1<<16)
    elif(_Codebit[0]=='0'):
        Offset=int(_Codebit[0:16],2)
    return Offset