
import I_type as itype
import J_type as jtype
import function as error_detect

def write(code):
    f = open('file/MachineCode.txt', 'a')
    f.write(code + '\n')
    f.close()

def read(filePath):
    file = open(filePath, 'r')
    label = []
    num_lines = sum(1 for line in open(filePath))
    for i in range(num_lines):
        s = file.readline()

        if s == '':  # check file end
            break
        instruction = s
        d = s.rstrip().split('\t');
        print('----------------------------------------------')
        print(d)
        # -------- Label ERROR!!! constraints check --------

        if d[0] != '':
            if (d[0] in label):
                print('ERROR label constraints!!!')
                break
        label.append(d[0])
        # ------------------ TYPE -------------------
        if d[1] == 'add' or d[1] == 'nand':
            # callR-type
            print('= R-type')
            #R_type.run_R_type(instruction)
        elif d[1] == 'lw' or d[1] == 'sw' or [1] == 'beq':
            # callI-type
            print('= I-type')
            mchcode = itype.iType(instruction)
        elif d[1] == 'halt' or d[1] == 'noop':
            # callO-type
            print('= O-type')
        elif d[1] == '.fill':
            # call.fill
            print('= .fill')
        elif d[1] == 'jalr':
            print('= J-type')
            mchcode = jtype.J_type(instruction)
        # ------------------------------------------
        error_detect.error_detect(mchcode) # Error detect function
        write(mchcode) # Write to file

    for u in range(len(label)):
        print('Address[', u , ']=', label[u])
    file.close()