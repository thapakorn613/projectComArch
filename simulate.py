import sys

filePath = sys.argv[1]
#filePath = 'file/machineCode.txt'

text_file = open(filePath, "r")
mem_machine_code = text_file.read().split('\n')
text_file.close()
pc = 0
register = ["00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000"]
MaxPc = sum(1 for line in open(filePath))

def addFormat(add_machine_code):
    regA = int(add_machine_code[10:13],2)
    regB = int(add_machine_code[13:16],2)
    destReg = int(add_machine_code[29:32],2)
    register[destReg] = decimalToBinary((binaryToDecimal(register[regA],32)+binaryToDecimal(register[regB],32)),32)
    return;

def nandFormat(nand_machine_code):
    regA=int(nand_machine_code[10:13],2)
    regB=int(nand_machine_code[13:16],2)
    destReg=int(nand_machine_code[29:32],2)
    register[destReg]=((int(register[regA],2) & int(register[regB],2)))
    register[destReg]=~register[destReg]
    register[destReg]=decimalToBinary(register[destReg],32)
    print (register[destReg])
    return;

def lwFormat(lw_machine_code):
    regA=int(lw_machine_code[10:13],2)
    regB=int(lw_machine_code[13:16],2)
    offset=str(lw_machine_code[16:32])
    register[regB]=mem_machine_code[(binaryToDecimal(offset,16)+binaryToDecimal(register[regA],32))]
    return;

def swFormat(sw_machine_code):
    regA = int(sw_machine_code[10:13],2)
    regB = int(sw_machine_code[13:16],2)
    offset = str(sw_machine_code[16:32])
    try:
        mem_machine_code[(binaryToDecimal(offset, 16) + binaryToDecimal(register[regA], 32))] = register[regB]
    except:
        mem_machine_code.append(register[regB])
    return;
    
def decimalToBinary(decimal,rangeOfbit):
    result = ''
    for x in range(rangeOfbit):
        r = decimal % 2
        decimal = decimal // 2
        result += str(r)
    result = result[::-1]
    return result

def binaryToDecimal(binary,rangeOfBit):
    if ( binary [0:1] == "0" ):
        return int(binary, 2)
    else:
        return int(binary, 2) - (1 << rangeOfBit);

def printMem():
    countmem = 0
    print("\t\tmemory:")
    outputSimulate.write("\t\tmemmory:" + "\n")
    for mem in mem_machine_code:
        try:
            print("\t\t\tmemmory[",countmem,"]",binaryToDecimal(mem, 32))
            outputSimulate.write("\t\t\tmemmory[" + str(countmem)+"]" + str(binaryToDecimal(mem, 32)) + "\n")
            countmem = countmem + 1
        except:
            return;

def printMemBegin():
    countmem = 0
    print ("\nRun of Simulator\n")
    outputSimulate.write("\nRun of Simulator\n")
    for mem in mem_machine_code:
        try:
            print("memmory[",countmem,"]",binaryToDecimal(mem, 32))
            outputSimulate.write("memmory[" + str(countmem)+"]" + str(binaryToDecimal(mem, 32)) + "\n")
            countmem = countmem + 1
        except:
            return;

def printRegister():
    print("\t\tregister:")
    countreg = 0
    outputSimulate.write("\t\tregister:"+"\n")
    for Reg in register:
        print("\t\t\treg[",countreg,"]",binaryToDecimal(Reg, 32))
        outputSimulate.write("\t\t\treg[" + str(countreg) + "]" + str(binaryToDecimal(Reg, 32))+"\n")
        countreg = countreg + 1
    outputSimulate.write("\n")
    print ("end state")


def printLastStage(stage, pc):
    print("machine halted")
    print("total of ", stage, " instructions executed")
    print("final state of machine:\n\n@@@")
    print("state:")
    print("\t\tpc:", pc)
    outputSimulate.write("machine halted")
    outputSimulate.write("total of "+str(stage)+" instructions executed")
    outputSimulate.write("final state of machine:\n\n@@@")
    outputSimulate.write("state:")
    outputSimulate.write("\t\tpc:" + str(pc))

def BEQ_I_TYPE(machine,PCindex):
    regA = int(machine[10:13], 2) #select_bit 21-19
    regB = int(machine[13:16], 2) #select_bit 18-16
    Offsetfield = str(machine[16:32])

    if(register[regA] == register[regB]):
        PCindex = PCindex+binaryToDecimal(Offsetfield, 16)
        return PCindex
    else:
        return PCindex

def JAIR_J_TYPE(machine,PCindex):
    regA = int(machine[10:13], 2) #select_bit 21-19 #keep address
    regB = int(machine[13:16], 2) #select_bit 18-16 #keep PC+1
    if (regA==regB):
        register[regA] = decimalToBinary((PCindex+1), 32)
        return PCindex
    else:
        register[regB] = decimalToBinary((PCindex+1), 32)
        PCindex =binaryToDecimal((register[regA]), 32)
        return PCindex

def simulate(mem_machine_code):
    stage = 1
    pc = 0
    pctest = 0
    printMemBegin()
    print("\n")
    while pc < MaxPc:
        pctest = pctest+1
        zerobit = (mem_machine_code[pc][16:31])
        obcode = mem_machine_code[pc][7:10]
        register[0] = "00000000000000000000000000000000"
        print ("@@@")
        print("state:",stage,"\n")
        outputSimulate.write("state: "+ str (stage)+"\n")
        print("\t\tpc:",pc)
        outputSimulate.write("\t\tpc:"+str(pc)+"\n")
        printMem()
        printRegister()
        print("\n")
        if obcode == "000" and zerobit!="0000000000000000":
            addFormat(mem_machine_code[pc])    
        elif obcode == "001":
            nandFormat(mem_machine_code[pc])    
        elif obcode == "010":
            lwFormat(mem_machine_code[pc])   
        elif obcode == "011":
            swFormat(mem_machine_code[pc])   
        elif obcode == "100":
            pc=BEQ_I_TYPE(mem_machine_code[pc],pc)
        elif obcode == "101":
            pc = (JAIR_J_TYPE(mem_machine_code[pc],pc))
            pc = pc-1
        elif obcode == "110":
            pc=pc+1
            printLastStage(stage,pc)
            printMem()
            printRegister()
            break;
        elif obcode == "111":
            print("noop")
        register[0] = "00000000000000000000000000000000"
        stage = stage + 1
        pc = pc + 1
    return;
outputSimulate = open("file/outputSimulate.txt","w")
simulate(mem_machine_code)
outputSimulate.close()