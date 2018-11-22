
import reg as reg
import mem as mem
import function as function
import J_type as jtype
import I_type as itype
import R_type as rtype
import O_type as otype
import toFile as toFile
import os
os.remove("file/MachineCode.txt")

filePath = "file/test2.txt"

print(toFile.read_for_label(filePath))
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
    label.append(d[0])
    # -------- Label ERROR!!! constraints check --------
    if len(d) > 4:
        if function.isint(d[4]) == False :
            d = toFile.check_for_label(d,i)
            print(d,'***')
            if d[4] == 'ERROR':
                print('ERROR Undefined Label!!!')
                break
            instruction = toFile.write_for_fill(d)

    # ------------------ TYPE -------------------
    if d[1] == 'add' or d[1] == 'nand':
        mchcode = rtype.rType(instruction)
        #toFile.write(mchcode)
        print("mcgcode[bin] : ",mchcode)
        print("mcgcode[dec] : ",function.binaryToDecimal(mchcode,32))
    elif d[1] == 'lw' or d[1] == 'sw' or d[1] == 'beq':
        # callI-type
        mchcode = itype.iType(instruction)
        print("mcgcode[bin] : "+mchcode)
        print("mcgcode[dec] : ",function.binaryToDecimal(mchcode,32))
    elif d[1] == 'halt' or d[1] == 'noop':
        # callO-type
        mchcode = otype.oType(instruction)
        print("mcgcode[bin] : "+mchcode)
        print("mcgcode[dec] : ",function.binaryToDecimal(mchcode,32))
    elif d[1] == 'jalr':
        mchcode = jtype.jType(instruction)
        #toFile.write(mchcode)
        print("mcgcode[bin] : "+mchcode)
        print("mcgcode[dec] : ",function.binaryToDecimal(mchcode,32))
    elif d[1] == '.fill' : 
        mchcode = toFile.dotFill(instruction)
        print("mcgcode[bin] : "+mchcode)
        print("mcgcode[dec] : ",function.binaryToDecimal(mchcode,32))
    # ------------------------------------------
    if d[1] != '.fill':
        function.error_detect(mchcode) # Error detect function
    toFile.write(mchcode) # Write to file
print('----------------------------------------------')
## test git hub
