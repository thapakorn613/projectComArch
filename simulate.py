
text_file = open("file\MachineCode.txt", "r")
mem_machine_code = text_file.read().split('\n')
#print(machine_code)
text_file.close()
pc=0
#register=["000","111","101","000","000","000","000","000"]
register=["00000000000000000000000000000000","00000000000000000000000000000111","00000000000000000000000000000101","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000"]
MaxPc = sum(1 for line in open('file\MachineCode.txt'))

#print(MaxPc)
def addFormat(add_machine_code):
    regA=int(add_machine_code[10:13],2)
    regB=int(add_machine_code[13:16],2)
    destReg=int(add_machine_code[29:32],2)
  #  print(" regA",regA)
   # print(" regB",regB)
   # print(" desReg",destReg)
    register[destReg]=decimalToBinary((binaryToDecimal(register[regA],32)+binaryToDecimal(register[regB],32)),32)
    return;

def nandFormat(nand_machine_code):
    regA=int(nand_machine_code[10:13],2)
    regB=int(nand_machine_code[13:16],2)
    destReg=int(nand_machine_code[29:32],2)
    #print(" regA",regA)
    #print(" regB",regB)
    #print(" desReg",destReg)
    register[destReg]=((int(register[regA],2) & int(register[regB],2)))
    register[destReg]=~register[destReg]
    register[destReg]=decimalToBinary(register[destReg],32)
    print (register[destReg])
    return;

def lwFormat(lw_machine_code):
    regA=int(lw_machine_code[10:13],2)
    regB=int(lw_machine_code[13:16],2)
    offset=str(lw_machine_code[15:32])
    register[regB]=decimalToBinary((binaryToDecimal(offset,16)+binaryToDecimal(register[regA],32)),16)
    return;

def swFormat(sw_machine_code):
    regA=int(sw_machine_code[10:13],2)
    regB=int(sw_machine_code[13:16],2)
    offset=str(sw_machine_code[15:32])
    print("regA",regA)
    print("regB",regB)
    print("offset",offset)
    print(binaryToDecimal("0011",4))
    print(binaryToDecimal(register[regA],32))
    print((binaryToDecimal(offset,16)+binaryToDecimal(register[regA],32)))
    mem_machine_code[(binaryToDecimal(offset,16)+binaryToDecimal(register[regA],32))]=regB
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
    if(binary[0:1]=="0"):
        print(binary[0:1])
        return int(binary, 2)
    else:
        print(binary[0:1])
        return  int(binary,2)-(1<<rangeOfBit);

def printMem():
    for mem in mem_machine_code:
        print(mem)

def printRegister():
     for Reg in register:
        print(Reg)

def simulate(mem_machine_code):
    for pc in range(MaxPc):
        #print(mem_machine_code[0])
        #print(mem_machine_code[0][0:7])
        obcode=mem_machine_code[pc][7:10]

        print(mem_machine_code[pc])

        if obcode=="000":
            print("add")
            #addFormat(mem_machine_code[pc])    
        elif obcode=="001":
            print("namd")
            nandFormat(mem_machine_code[pc])    
        elif obcode=="010":
            print("lw")
            #lwFormat(mem_machine_code[pc])   
        elif obcode=="011":
            print("sw")
            #swFormat(mem_machine_code[pc])   
        elif obcode=="100":
            print("beq")
        elif obcode=="101":
            print("jalr")
        elif obcode=="110":
            print("halt")
        elif obcode=="111":
            print("noop")
    printMem()
    printRegister()
    return;

simulate(mem_machine_code)