#!/usr/bin/python\
import reg as reg
import mem as mem
import function as function
import  J_type as jtype
import I_type as itype

instruction="start jalr   2   4" # test J type
opcode = ""
f = open('file/program','r')
message = f.read()
f.close()

# --------------- Beginnig I type ---------
machineLanguage = itype.iType(message)
print ("machineLanguage [ I type ] : " + machineLanguage)
print ("machineLanguage [ J type ] :  : "+ jtype.J_type(instruction))