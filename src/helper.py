import re
from init import Instructions, R_type, I_type, J_type

# 获得标签
label_pattern = r'^[a-zA-Z0-9_]+$'

def getLabel(line:str):
    if re.match(label_pattern, line):
        return line
    else:
        raise SyntaxError("标签中只能出现字母, 数字和下划线!")
        
        
# 获得指令类型, 并将指令及其寄存器存在对应的键值对中,
# R_type, I_type, J_type
def getInstructionType(line:str):
    line = line.strip()
    pos_cmd = line.find(' ')
    try:
        cmd = line[0:pos_cmd]
        pos = Instructions.index(cmd)
        
        line = line[pos_cmd + 1:]
        line = line.replace(" ", "")
          
        if pos == -1:
            raise SyntaxError("指令不存在!, 目前仅支持R,I,J类型的指令(书写指令必须与寄存器有空格)")
        if pos < 20:
            storeRType(line)
            return "R"
        elif pos < 37:
            storeIType(line)
            return "I"
        else:
            storeJType(line)
            return "J"
        
    except SyntaxError as e:
        print(e)



def storeRType(line:str):
    pass


IType_pattern = r"\$(\w+),\$(\w+),(\d+)"
def storeIType(line:str):
    try:
        match = re.search(IType_pattern, line)
        if match:
            R_type["rt"] = match.group(1)
            R_type["rs"] = match.group(2)
            R_type["const"] = int(match.group(3))
        
        else:
            raise SyntaxError("指令格式书写错误!")
    except SyntaxError as e:
        print(e)
        


def storeJType(line:str):
    try:
        match = re.match(label_pattern, line)
        if match:
            J_type["address"] = line
        
        else:
            raise SyntaxError("标签中只能出现字母, 数字和下划线!")
    
    except SyntaxError as e:
        print(e)
        

if __name__ == "__main__":        
    string = "j label_1\n"
    print(J_type["address"])
    print(getInstructionType(string))
    print(J_type["address"])