import function as convert
def create_register(num):                                                    #functio นี้ใช้สำหรับเเปลงค่า register  ที่รับเป็นฐาน10 ให้เป็น ฐาน2
    num = int(num)
    keepnum = ""
    for i in range(3):
        if ((num >> i) & 1 == 1):                                            #ทำงานโดยการเช็คที่ละbitว่าเป็น 1 หรือ 0 เเล้วจะเพิ่ม char 
            keepnum += '1'
        else:
            keepnum += '0'
    return keepnum[::-1]                                                     #การทำงานจะเป็นจากหลังมาหน้าดังนั้นจึงต้องทำการ reverse string

def create_machine(case, num1, num2, num3):                                  #ใช้สำหรับการสร้าง machine code โดยเเยกเป็น case ฟืก กับ nand
    zero = "0000000"                                                         #โดยจะรับค่า register ที่เเปลงเป็น binary เเล้ว
    if case == "add":
        opcode = "000"
    elif case == "nand":
        opcode = "001"
    othernum = "0000000000000"
    alll = zero + opcode + num1 + num2 + othernum + num3                     #return ทุกค่ารวมกันเป็น machine code
    return alll



def rType(instruction):                                                      #ใช้เเยก assembly code ออกเป็นส่วนๆ
    name = ""
    name += instruction
    keep_type = ""
    num1 = ""
    num2 = ""
    num3 = ""
    num = name.find('\t')                                                    #num = ตำเเหน่งของการ tab ครั้งเเรก
    # start add x1 x2 x3
    for i in range(len(name)):                                               #เพิ่มค่า num ไปเรื่อยๆ จนกว่าจะเจอตำเเหน่งที่ไม่ใช่ tab
        if (name[num + i] != '\t'):                                          #ซึ่งก็คือตำเเหน่งเเรกของ name of instruction
            num = num + i
            break;


    nums = name.find('\t', num + 1)                                          #num = ตำเเหน่งของการ tab หลังจาก num 
                                                                             #ซึ่งก็คือตำเเหน่งเเรกของtab หลังจาก name of instruction
    for i in range(nums - num):
        keep_type = keep_type + name[i + num]                                #เพิ่มค่าname of instructionให้ keep_type เเต่ละตัวจนครบ

    for i in range(len(name)):                                               #หาตำเเหน่งที่ไม่ไช่ tab หลัง nums
        if (name[nums + i] != '\t'):                                         #ซึ่งก็คือตำเเหน่งเเรกของ register ตัวที่ 1
            num = nums + i
            break;

    for i in range(len(name)):                                               #หาตำเเหน่งที่เป็น tab หลัง num
        if (name[num + i] == '\t'):                                          #ซึ่งก็คือตำเเหน่งเเรกของ tab หลัง register ตัวที่ 1
            nums = num + i
            break;

    keep1 = num
    for i in range((nums - num)):                                            #เพิ่มค่าregister ตัวที่ 1 ให้ num1 เเต่ละตัวจนครบ
        num1 += name[keep1]
        keep1 = keep1 + 1

    for i in range(len(name)):                                               #หาตำเเหน่งที่ไม่ไช่ tab หลัง nums
        if (name[nums + i] != '\t'):                                         #ซึ่งก็คือตำเเหน่งเเรกของ register ตัวที่ 2
            num = nums + i
            break;

    for i in range(len(name)):                                               #หาตำเเหน่งที่เป็น tab หลัง num
        if (name[num + i] == '\t'):                                          #ซึ่งก็คือตำเเหน่งเเรกของ tab หลัง register ตัวที่ 2                                    
            nums = num + i
            break;

    keep2 = num
    for i in range((nums - num)):                                            #เพิ่มค่าregister ตัวที่ 2 ให้ num2 เเต่ละตัวจนครบ
        num2 += name[keep2]
        keep2 = keep2 + 1

    for i in range(len(name)):                                               #หาตำเเหน่งที่ไม่ไช่ tab หลัง nums
        if (name[nums + i] != '\t'):                                         #ซึ่งก็คือตำเเหน่งเเรกของ register ตัวที่ 3
            num = nums + i
            break;

    nums = len(name)                                                         #หาตำเเหน่งที่ไม่ไช่ tab จากหลังมาหน้า
    for i in range(len(name)):                                               #ซึ่งก็คือตำเเหน่งสุดท้ายของ register ตัวที่ 3
        if (name[nums - 1] != '\t'):
            break;
        nums = nums - 1

    keep3 = num

    for i in range((nums - num)-1):                                          #เพิ่มค่าregister ตัวที่ 3 ให้ num3 เเต่ละตัวจนครบ
        num3 += name[keep3]
        keep3 += 1
    print(num3)
    tempnum3 = int(num3)                                                            #เปลี่ยน register ทุกตัวให้เป็น int
    tempnum2 = int(num2)
    tempnum1 = int(num1)
    num3 = convert.numToBinary(tempnum3, 3)                                         #เปลี่ยนnumทุกตัวให้เป็น binary
    num2 = convert.numToBinary(tempnum2, 3)
    num1 = convert.numToBinary(tempnum1, 3)
    
    return create_machine(keep_type, num1, num2, num3)                              #เรียกใช้งาน function ที่เ็น machine code

#run_R_type("start      nand      55  22  33    ")
