text_file = open("MachineCode.txt", "r")
mem_machine_code = text_file.read().split('\n')
text_file.close()
MaxPc = sum(1 for line in open('MachineCode.txt'))
registers=[0,5,-1,0,0,0,0,0]
def BEQ_I_TYPE(machine,PCindex):
    
    regA = int(machine[10:13],2) #select_bit 21-19
    regB = int(machine[13:16],2) #select_bit 18-16
    Offsetfield = machine[16:] #select_bit 15-0
    
    print "\t\tBEQ"
    
    if(registers[regA] == registers[regB]):
        PCindex=PCindex+CovertTwocomplement(Offsetfield)
        print "JUME !!"
        return PCindex
    else:
        print "NOT JUME !!"
        return PCindex

def JAIR_J_TYPE(machine,PCindex):
    
    regA = int(machine[10:13],2) #select_bit 21-19 #keep address
    regB = int(machine[13:16],2) #select_bit 18-16 #keep PC+1
    
    print "\t\tJAIR"
    
    if (registers[regA]==registers[regB]):
        
        registers[regA,regB] = PCindex+1
        
        return PCindex
    else:
        registers[regB] = PCindex+1
        PCindex = registers[regA]
        
        return PCindex

    
def HAIT_O_TYPE():
    
    print "\t\tHALT"
    
def NOOP_O_TYPE():
    
    print "\t\tNOOP"
    
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
    pc_count=0
    pc_idex=0
    startProgram = True
    while startProgram:
        
        machineCode = mem_machine_code[pc_count]
        opCode = machineCode[7:10]
        
        print ("status :")
        print "\tPC [%(PCcount)d]"  % {"PCcount": pc_count}

        #print ("\t\ttotal :"+opCode+regA+regB+Other)
        #print ("\t\tOpcode :"+opCode)
        #print ("\t\tregA :"+regA)
        #print ("\t\tregB :"+regB)
        #print ("\t\tOther :"+Other)
        print "\tMEM :"
        for x in  range(0,MaxPc):
            #print mem_machine_code[x]
            print "\t\tmem[%(pc)d]: %(memory)d -->%(machinebit)d Bit" \
                  %{"pc": x ,"memory" : binToDecimal(mem_machine_code[x])
                      ,"machinebit":len(mem_machine_code[x])}
           
        print "\tREGISTERS :"
        for y in range(len(registers)):
            print "\t\treg[%(register)d]: %(valueInreg)d" %{"register" : y,"valueInreg" : registers[y]}
    
        if(opCode=='100'):
            
            pc_count=BEQ_I_TYPE(machineCode,pc_count)
            
        elif(opCode == '101'):
            
            pc_count=JAIR_J_TYPE (machineCode,pc_count)-1
        
        elif(opCode == '110'):
            
            HAIT_O_TYPE()
            
        elif(opCode == '111'):
            
            NOOP_O_TYPE()
            
        elif(opCode == '000'):
            #Test opcode add
            registers[1] = registers[1]-1
            
        else:
            print ("\t\tInvalid Opcode")
        
        
        print "end status"
        
        if(mem_machine_code[pc_count+1][7:10]=='110'):
            print "machine halted"
            print "total of %(totalpc)d instructions executed" %{"totalpc":pc_idex+1}
            print "final state of machine :"
        elif(mem_machine_code[pc_count][7:10]=='110'):
            startProgram = False
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        pc_count=pc_count+1
        pc_idex=pc_idex+1
    return;


simulate(mem_machine_code)
#print CovertTwocomplement('1111111111111111')

