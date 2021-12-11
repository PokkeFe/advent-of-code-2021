#!env python

def filter_values(arr, pos, char):
    new_arr = []
    for val in arr:
        if val[pos] == char:
            new_arr.append(val)
    return new_arr

values = []
line_count = 0

with open("input") as input:
    line = input.readline()

    while line != "":
        values.append(line[:-1])
        line = input.readline()

    o2gen = values.copy()

    bit_pos = 0
    while len(o2gen) > 1:
        bit_count = 0
        for v in o2gen:
            if v[bit_pos] == "1":
                bit_count += 1
        if (bit_count * 2) >= len(o2gen):
            o2gen = filter_values(o2gen, bit_pos, "1")
        else:
            o2gen = filter_values(o2gen, bit_pos, "0")
        bit_pos += 1

    co2scrub = values.copy()

    bit_pos = 0
    while len(co2scrub) > 1:
        bit_count = 0
        for v in co2scrub:
            if v[bit_pos] == "1":
                bit_count += 1
        if (bit_count * 2) >= len(co2scrub):
            co2scrub = filter_values(co2scrub, bit_pos, "0")
        else:
            co2scrub = filter_values(co2scrub, bit_pos, "1")
        bit_pos += 1

    o2gen_rating = int(o2gen[0], 2)
    co2scrub_rating = int(co2scrub[0], 2)

    print(f"life support rating: {o2gen_rating * co2scrub_rating}")
