#!env python

depth = 0
pos = 0

with open("input") as input:
    line = input.readline()
    while line != "":
        command = line[:-1].split(' ')
        instr = command[0]
        val = int(command[1])
        if instr == "forward":
            pos += val
        elif instr == "down":
            depth += val
        elif instr == "up":
            depth -= val
        
        line = input.readline()
    
    print(f"depth * pos = {depth * pos}")