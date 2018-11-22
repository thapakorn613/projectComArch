
text_file = open("file\MachineCode.txt", "r")
mem_machine_code = text_file.read().split('\n')
#print(machine_code)
text_file.close()
pc=0
#register=["000","111","101","000","000","000","000","000"]
register=["00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000"]
MaxPc = sum(1 for line in open('file\MachineCode.txt'))

#print(MaxPc)
def addFormat(add_machine_code):
    regA=int(add_machine_code[10:13],2)
    regB=int(add_machine_code[13:16],2)
    destReg=int(add_machine_code[29:32],2)
    print(" regA",regA)
    print(" regB",regB)
    print(" desReg",destReg)
    register[destReg]=decimalToBinary((binaryToDecimal(register[regA],32)+binaryToDecimal(register[regB],32)),32)
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
    print(offset)
    print(register[regA])
    print(regB)
    print("mem_machine_code[(binaryToDecimal(offset,16)+binaryToDecimal(register[regA],32))]",mem_machine_code[(binaryToDecimal(offset,16)+binaryToDecimal(register[regA],32))])
    register[regB]=mem_machine_code[(binaryToDecimal(offset,16)+binaryToDecimal(register[regA],32))]
    return;

def swFormat(sw_machine_code):
    regA=int(sw_machine_code[10:13],2)
    regB=int(sw_machine_code[13:16],2)
    offset=str(sw_machine_code[16:32])
    print("regA",regA)
    print("regB",regB)
    print("offset",offset)
  
    print(binaryToDecimal(register[regA],32))
    print(binaryToDecimal(offset,16))
    print((binaryToDecimal(offset,16)+binaryToDecimal(register[regA],32)))
    print(register[regB])
    mem_machine_code[(binaryToDecimal(offset,16)+binaryToDecimal(register[regA],32))]=register[regB]
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
        #print(binary[0:1])
        return int(binary, 2)
    else:
        #print(binary[0:1])
        return  int(binary,2)-(1<<rangeOfBit);

def printMem():
    countmem=0
    print("memory:")
    for mem in mem_machine_code:
        try:
            print("memmory[",countmem,"]",binaryToDecimal(mem,32))
            #print("memmory[",countmem,"]",mem)
            countmem=countmem+1
        except:
            return;
   
        

def printRegister():
    print("register:")
    countreg=0
    for Reg in register:
        #print(Reg)
        print("reg[",countreg,"]",binaryToDecimal(Reg,32))
        #print("reg[",countreg,"]",Reg)
        countreg=countreg+1

def BEQ_I_TYPE(machine,PCindex):
    regA = int(machine[10:13],2) #select_bit 21-19
    regB = int(machine[13:16],2) #select_bit 18-16
    Offsetfield=str(machine[16:32])

    
    if(register[regA] == register[regB]):
        PCindex=PCindex+binaryToDecimal(Offsetfield,16)
        print ("JUME !!")
        print (PCindex)
        print((Offsetfield))
        print(binaryToDecimal(Offsetfield,16))
        print(PCindex)
        return PCindex
    else:
        print ("NOT JUME !!")
        return PCindex

def JAIR_J_TYPE(machine,PCindex):
    
    regA = int(machine[10:13],2) #select_bit 21-19 #keep address
    regB = int(machine[13:16],2) #select_bit 18-16 #keep PC+1
    
    print ("\t\tJAIR")
    
    if (regA==regB):
        
        register[regA] = decimalToBinary((PCindex+1),32)
        
        return PCindex
    else:
        register[regB] = decimalToBinary((PCindex+1),2)
        PCindex =binaryToDecimal((register[regA]),32)
        print(PCindex)
        return PCindex

    
def HAIT_O_TYPE():
    return;
    
   # print ("\t\tHALT")
    
def NOOP_O_TYPE():
    return;
   # print ("\t\tNOOP")
    
def CovertTwocomplement(_Codebit):
    
    Offset=0

    if(_Codebit[0]=='1'):
        
        Offset=int(_Codebit[0:16],2)-(1<<16)
        
    elif(_Codebit[0]=='0'):
        
        Offset=int(_Codebit[0:16],2)
        
    return Offset
def binToDecimal(str):
    n = 0
    temp = 0
    sum = 0
    str_exe = list (str)
    if(str[0:17]=='00000000000000001'):
        
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


def simulate(mem_machine_code):
    printMem()
    stage=0
    print("stage:",stage)
    print("pc:0")
    printMem()
    printRegister()
    pc=0
    pctest=0
    print("\n\n\n")
    while pctest < (20):
        pctest=pctest+1
        print("pc:",pc+1)
        #print(mem_machine_code[0])
        zerobit=(mem_machine_code[pc][16:31])
        obcode=mem_machine_code[pc][7:10]
        
        #print(mem_machine_code[pc])

        if obcode=="000" and zerobit!="0000000000000000":
            print("add")
            addFormat(mem_machine_code[pc])    
        elif obcode=="001":
            print("namd")
            nandFormat(mem_machine_code[pc])    
        elif obcode=="010":
            print("lw")
            lwFormat(mem_machine_code[pc])   
        elif obcode=="011":
            print("sw")
            swFormat(mem_machine_code[pc])   
        elif obcode=="100":
            print("beq")
            pc=BEQ_I_TYPE(mem_machine_code[pc],pc)
        elif obcode=="101":
            print("jalr")
            pc=(JAIR_J_TYPE(mem_machine_code[pc],pc))+1
        elif obcode=="110":
            print("halt")
            printMem()
            printRegister()
            HAIT_O_TYPE()
            break;
        elif obcode=="111":
            print("noop")
            NOOP_O_TYPE()
        if(obcode!="---"):
            register[7]="00000000000000000000000000000000"
            print("stage:",stage)
            printMem()
           
            printRegister()
            stage=stage+1
            pc=pc+1
            print("\n\n\n")
    return;

simulate(mem_machine_code)