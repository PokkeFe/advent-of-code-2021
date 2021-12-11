#!env python

def sum(arr):
    s = 0
    for i in arr:
        s += i
    return s

with open("input") as input:
    q = []

    for i in range(3):
        line = input.readline()
        q.append(int(line[:-1]))
    
    depth_increases = 0
    last_measure = sum(q)
    q.pop(0)
    
    line = input.readline()
    while(line != ""):
        q.append(int(line[:-1]))
        new_measure = sum(q)
        q.pop(0)
        if new_measure > last_measure:
            depth_increases += 1
        last_measure = new_measure
        line = input.readline()
    
    print(f"depth increases: {depth_increases}")
