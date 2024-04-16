from init import *
from helper import *
import re

def loadInstruction(line):
    line = line.strip()
    # print(line)
    if ':' in line:
        label_end = line.find(':')
        
        try:
            label = getLabel(line[0: label_end])
        
        except SyntaxError as e:
            print(e)
        
        label_position[label] = PC - 1
        
        if line[label_end + 1:]:
            line = line[label_end + 1:]
    
    instruction = getInstructionType(line)
    
    execution()
        
        
if __name__ == "__main__":
    loadInstruction("label:\n")