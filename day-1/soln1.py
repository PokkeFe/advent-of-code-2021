#!env python

with open("input") as input:
    line = input.readline()
    depth = int(line[:-1])
    depth_increases = 0

    line = input.readline()
    while(line != ""):
        new_depth = int(line[:-1])
        if new_depth > depth:
            depth_increases += 1
        depth = new_depth
        line = input.readline()
    
    print(f"depth increases: {depth_increases}")
