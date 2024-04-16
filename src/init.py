# 分R, I, J的顺序
R_start = 0
I_start = 20
J_start = 37
Instructions = ["add", "addu", "and", "jr", "nor", "or", "slt", "sltu", "sll", "srl", 
               "sub", "subu", "div", "divu", "mfhi", "mflo", "mfc0", "mult", "multu", 
               "sra", "addi", "addiu", "andi", "beq", "bne", "lbu", "lhu", "ll", "lui",
               "lw", "ori", "slti", "sltiu", "sb", "sc", "sh", "sw", "j", "jal"]

Reg = {
    "zero": 0, "at": 0, "v0": 0, "v1": 0,
    "a0": 0, "a1": 0, "a2": 0, "a3": 0,
    "t0": 0, "t1": 0, "t2": 0, "t3": 0, "t4": 0, "t5": 0, "t6": 0, "t7": 0, "t8": 0, "t9": 0, 
    "s0": 0, "s1": 0, "s2": 0, "s3": 0, "s4": 0, "s5": 0, "s6": 0, "s7": 0,
    "k0": 0, "k1": 0, 
    "gp": 0, "sp": 0, "fp": 0, "ra": 0
}

PC = 1

MEMORY = []

R_type = {
    "opcode": "",
    "rd": "",
    "rs": "",
    "rt": "",
    "shamt": 0,
}

I_type = {
    "opcode": "",
    "rd": "",
    "rt": "",
    "const": 0
}

J_type = {
    "opcode": "",
    "address": "",
}

label_position = {}