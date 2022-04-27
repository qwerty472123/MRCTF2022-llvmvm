ll = open('part_of_func1.c').read().strip().splitlines()
for i in range(0, len(ll), 12):
    a = ll[i+0].split('memory[0x98] = [unsigned int* (4 * ')[-1].split(' + ')[0]
    b = ll[i+1].split('memory[0x9c] = [unsigned int* (4 * ')[-1].split(' + ')[0]
    pre = ll[i+3].split('memory[0x94] = (int)memory[0x90] >> (int)')[-1].split(';')[0]
    dest = ll[i+8].split('memory[0x90] = 4 * ')[-1].split(' + tmp;')[0]
    print(f"    ({dest}, {a}, {b}, {pre}), ")
