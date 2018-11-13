def oType (assembly):
    zero = "00000000"
    zeroOfInstruction = "000000000000000000000"
    inst = assembly.split('\t')
    inst[1] = str(inst[1])
    print("inst[1]:"+inst[1])
    if ( inst[1] == 'halt'):
        opcode = '110'
    elif ( inst[1] == 'noop'):
        opcode = '111'
    else:
        opcode = 'error'
    MachineCode = zero + opcode + zeroOfInstruction
    return MachineCode



