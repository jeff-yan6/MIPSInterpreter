import sys
from src.init import *
from src.func import *



def readFile(filename:str):
    with open(filename, "w") as file:
        file.seek(PC)
        PC += 1
        line = file.readline
        loadInstruction(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("please choose file to interpreter!")
    elif len(sys.argv) > 2:
        print("I can only interpreter one file one time!")
    else:
        readFile(sys.argv[1])
    