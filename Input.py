print('Welcome to compiler :)')

file = open('myconfig.txt', 'r')


label = []

for i in range(88):
    s = file.readline()

    if s == '':  # check file end
        break

    d = s.rstrip().split('\t');
    print(d[1])
    label.append(d[0])

    if d[1] == 'add' or d[1] == 'nand':
        # callR-type
        print('=R-type')
    elif d[1] == 'lw' or d[1] == 'sw' or d[1] == 'beq':
        # callI-type
        print('=I-type')
    elif d[1] == 'halt' or d[1] == 'noop':
        # callO-type
        print('=O-type')
    elif d[1] == '.fill':
        # call.fill
        print('=.fill')
    elif d[1] == 'jalr':
        print('=J-type')

print(label)

file.close()


