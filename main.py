#!/usr/bin/python\
import reg as reg
import mem as mem
import function as function
import J_type as jtype
import I_type as itype
import R_type as rtype
import O_type as otype
import toFile as toFile

instruction="start jalr   2   4" # test J type

filePath = "file/testAllFunction.txt"


toFile.read_for_fill(filePath)
file = open(filePath, 'r')
label = []
num_lines = sum(1 for line in open(filePath))
for i in range(num_lines):
    mchcode='--------------------------------'
    s = file.readline()
    if s == '':  # check file end
        break
    instruction = s
    d = s.rstrip().split('\t');
    print('----------------------------------------------')
    print(d)
    # -------- Label ERROR!!! constraints check --------
    if len(d) > 4:
        if function.isint(d[4]) == False :
            d[4] = toFile.check_for_fill(d[4])
            print(d,'***')
            if d[4] == 'ERROR':
                print('ERROR Undefined Label!!!')
                break
            instruction = toFile.write_for_fill(d)
    if d[0] != '':
        if (d[0] in label):
            print('ERROR label constraints!!!')
            break
    label.append(d[0])
    # ------------------ TYPE -------------------
    if d[1] == 'add' or d[1] == 'nand':
        # callR-type
        print('= R-type')
        #mchcode = rtype.run_R_type(instruction)
    elif d[1] == 'lw' or d[1] == 'sw' or d[1] == 'beq':
        # callI-type
        print('= I-type')
        mchcode = itype.iType(instruction)
    elif d[1] == 'halt' or d[1] == 'noop':
        # callO-type
        print('= O-type')
        mchcode = otype.oType(instruction)
        print("mcgcode : "+ mchcode)
    elif d[1] == '.fill':
        # call.fill
        print('= .fill')
    elif d[1] == 'jalr':
        print('= J-type')
        mchcode = jtype.J_type(instruction)
    # ------------------------------------------
    function.error_detect(mchcode) # Error detect function
    toFile.write(mchcode) # Write to file
print('----------------------------------------------')



# --------------- Beginnig I type ---------
#machineLanguage = itype.iType(machineLanguage)
#print ("machineLanguage [ I type ] : " + machineLanguage)
#print ("machineLanguage [ J type ] :  : "+ jtype.J_type(instruction))