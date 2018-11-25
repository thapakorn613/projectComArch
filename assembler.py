import function as function
import J_type as jtype
import I_type as itype
import R_type as rtype
import O_type as otype
import toFile as toFile
import os
import sys
os.remove("file\machineCode.txt")
filePath = sys.argv[1]
print(toFile.read_for_label(filePath))
toFile.read_for_fill(filePath)
file = open(filePath, 'r')
label = []
num_lines = sum(1 for line in open(filePath))
for i in range(num_lines):
    mchcode = '--------------------------------'
    s = file.readline()
    if s == '':  # check file end
        break
    instruction = s
    d = s.rstrip().split('\t');
    label.append(d[0])
    if len(d) > 4:
        if function.isint(d[4]) == False :
            d = toFile.check_for_label(d,i)
            print(d,'***')
            if d[4] == 'ERROR':
                print('ERROR Undefined Label!!!')
                break
            instruction = toFile.write_for_fill(d)
    if d[1] == 'add' or d[1] == 'nand':
        mchcode = rtype.rType(instruction)
    elif d[1] == 'lw' or d[1] == 'sw' or d[1] == 'beq':
        mchcode = itype.iType(instruction)
    elif d[1] == 'halt' or d[1] == 'noop':
        mchcode = otype.oType(instruction)
    elif d[1] == 'jalr':
        mchcode = jtype.jType(instruction)
    elif d[1] == '.fill' : 
        mchcode = toFile.dotFill(instruction)
    if d[1] != '.fill':
        function.error_detect(mchcode) # Error detect function
    toFile.write(mchcode) # Write to file
