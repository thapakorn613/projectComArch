
import I_type as itype
import J_type as jtype
import function as error_detect

def write(code):
    f = open('file/MachineCode.txt', 'a')
    f.write(code + '\n')
    f.close()
def write_for_fill(code):
    f = open('file/fillcode.txt', 'w')
    for i in range(len(code)):
        if code[i] != '':
            f.write('\t' + code[i])

    f = open('file/fillcode.txt', 'r')
    s = f.readline()
    f.close()
    return s

filllist = []
filllist2 = []

numline = 0
def read_for_fill(filePath):
    file = open(filePath, 'r')

    num_lines = sum(1 for line in open(filePath))
    for i in range(num_lines):
        s = file.readline()

        if s == '':  # check file end
            break

        fill = s.rstrip().split('\t');
        if fill[1] == '.fill':
            filllist.append(fill)
    print(filllist)
    #print(len(filllist[0]))

def check_for_fill(fillcheck):
    for i in range(len(filllist)):
        filllist2.append(filllist[i][0])
           # return filllist[i][2]
    print(filllist2)
    print(fillcheck)
    if fillcheck in filllist2:
        #return  filllist2[i]
        filllist2.clear()
        print('im here')
        for j in range(len(filllist)):
            if fillcheck == filllist[j][0]:
                return filllist[j][2]
    else: #print('ERROR Undefined Label!!!')
        return 'ERROR'
    return 'ERROR'

def isint(value):
      try:
        int(value)
        return True
      except ValueError:
        return False






def read(filePath):
    read_for_fill(filePath)
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

            if isint(d[4]) == False :
                d[4]=check_for_fill(d[4])
                print(d,'***')
                if d[4] == 'ERROR':
                    print('ERROR Undefined Label!!!')
                    break
                #instruction = d
                instruction = write_for_fill(d)
                #print(instruction)
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
        print('Address[', u, ']=', label[u])
    #return mchcode
    file.close()