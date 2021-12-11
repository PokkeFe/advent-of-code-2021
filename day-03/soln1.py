#!env python

bit_counts = []
line_count = 0

with open("input") as input:
    line = input.readline()

    for char in line[:-1]:
        if char == "1":
            bit_counts.append(1)
        else:
            bit_counts.append(0)
    line_count += 1

    while line != "":
        for index, char in enumerate(line[:-1]):
            if char == "1":
                bit_counts[index] += 1
        
        line_count += 1
        
        line = input.readline()
    
    epsilon = ""
    gamma = ""
    
    half_lc = int(line_count / 2)
    for count in bit_counts:
        if count > half_lc:
            gamma += "1"
            epsilon += "0"
        else:
            epsilon += "1"
            gamma += "0"
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(f"power consumption: {gamma * epsilon}")
