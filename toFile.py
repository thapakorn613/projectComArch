import function as function
import sys
import os
filePath2 = 'file/machineCode.txt'
filllist = []
filllist2 = []
numline = 0
label = []
labellist = []

def numToBinary(n,rangeOffbit):
    result = ''
    for x in range(rangeOffbit):
        r = n % 2
        n = n // 2
        result += str(r)
    result = result[::-1]
    return result

def write(code):
    f = open(filePath2, 'a')
    f.write(code + '\n')
    f.close()

def write_for_fill(code):
    f = open('file/temp.txt', 'w')
    for i in range(len(code)):
        f.write(code[i] + '\t')

    f = open('file/temp.txt', 'r')
    s = f.readline()
    f.close()
    return s



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



def read_for_label(filePath):
    file = open(filePath, 'r')
    num_lines = sum(1 for line in open(filePath))
    for i in range(num_lines):
        s = file.readline()

        if s == '':
            break

        label = s.rstrip().split('\t');
        if label[0] != '':
            if (label[0] in labellist):
                print('ERROR label constraints!!!')
                break
        labellist.append(label[0])
    return labellist

def check_for_label(labelcheck,addr):
    #print(labelcheck,addr)
    if labelcheck[4] not in labellist:
        print('ERROR Undenfined Label!!****!')
        quit()
    for i in range(len(labellist)):
        #print(labelcheck[4])


        if labelcheck[4] == labellist[i]:
            if labelcheck[1] == 'lw' or labelcheck[1] == 'sw':
                #labelcheck[4] = str(i + int(labelcheck[2]))
                labelcheck[4] = str(i)
            elif labelcheck[1] == 'beq':
                labelcheck[4] = str(i - addr - 1)
                #labelcheck[4] = str(i)
    return labelcheck





def dotFill(msg):
    line = 0
    msg_split = msg.rstrip().split('\t');
    match_label = msg_split[2]
    is_match_label_int = function.isint(match_label)
    if(is_match_label_int == False):
        if match_label in labellist:
            line = int(labellist.index(match_label)) # found label line
    else:
        line = match_label
        
    offsetField = numToBinary(int(line), 32) # convert offsetfield to binary

    return offsetField
