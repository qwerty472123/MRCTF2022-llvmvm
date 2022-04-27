import re
import struct

with open("code.bin", "rb") as f:
    code = f.read()


class vm_instr:

    def __init__(self, name: str, instr_size: int, stackcost: int, func):
        self.name = name
        self.instr_size = instr_size
        self.stackcost = stackcost
        self.func = func

    def pack(self, operators: list):
        self.comment = self.func(operators)


opcode_tbl = {
    0x01:
    vm_instr(name="INSTR_OP01",
             instr_size=1,
             stackcost=-2,
             func=lambda operators: "[QWORD* memory[{}]] = memory[{}]".format(
                 hex(operators[1]), hex(operators[0]))),
    0x02:
    vm_instr(name="INSTR_OP02",
             instr_size=1,
             stackcost=-2,
             func=lambda operators: "[unsigned int* memory[{}]] = memory[{}]".
             format(hex(operators[1]), hex(operators[0]))),
    0x03:
    vm_instr(name="INSTR_OP03",
             instr_size=1,
             stackcost=-2,
             func=lambda operators: "memory[{}] = (unsigned int*) memory[{}]".
             format(hex(operators[1]), hex(operators[0]))),
    0x04:
    vm_instr(
        name="INSTR_OP04",
        instr_size=5,
        stackcost=-1,
        func=lambda operators: "if (memory[{}])".format(hex(operators[0]))),
    0x05:
    vm_instr(name="INSTR_OP05",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[OP] = [unsigned int* memory[{}]]".
             format(hex(operators[0]))),
    0x06:
    vm_instr(name="INSTR_OP06",
             instr_size=5,
             stackcost=-2,
             func=lambda operators: "memory[OP] = BYTE memory[{}] < memory[{}]"
             .format(hex(operators[0]), hex(operators[1]))),
    0x07:
    vm_instr(name="INSTR_OP07",
             instr_size=5,
             stackcost=-3,
             func=lambda operators:
             "memory[OP] = !memory[{}] ? memory[{}] : memory[{}]".format(
                 hex(operators[0]), hex(operators[2]), hex(operators[1]))),
    0x08:
    vm_instr(name="INSTR_OP08",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[OP] = [int* memory[{}]]".format(
                 hex(operators[0]))),
    #  comment="write memory[stack[0]] to memory[opcode] like 05?"),
    0x09:
    vm_instr(
        name="INSTR_OP09",
        instr_size=5,
        stackcost=-1,
        func=lambda operators: "memory[OP] = memory[{}]".format(hex(operators[0]))),
    0x0a:
    vm_instr(name="INSTR_OP0A",
             instr_size=5,
             stackcost=-2,
             func=lambda operators:
             "memory[OP] = (char)memory[{}] + (long)memory[{}]".format(
                 hex(operators[0]), hex(operators[1]))),
    0x0b:
    vm_instr(name="INSTR_OP0B",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[OP] = [BYTE* memory[{}]]".format(
                 hex(operators[0]))),
    0x0c:
    vm_instr(
        name="INSTR_OP0C",
        instr_size=5,
        stackcost=-1,
        func=lambda operators: "memory[OP] = memory[{}]".format(hex(operators[0]))),
    0x0d:
    vm_instr(
        name="INSTR_OP0D",
        instr_size=5,
        stackcost=-2,
        func=lambda operators: "memory[OP] = (int)memory[{}] + (int)memory[{}]"
        .format(hex(operators[0]), hex(operators[1]))),
    0x0e:
    vm_instr(
        name="INSTR_OP0E",
        instr_size=5,
        stackcost=-2,
        func=lambda operators: "memory[OP] = (int)memory[{}] ^ (int)memory[{}]"
        .format(hex(operators[0]), hex(operators[1]))),
    0x0f:
    vm_instr(
        name="INSTR_OP0F",
        instr_size=5,
        stackcost=-2,
        func=lambda operators: "memory[OP] = (int)memory[{}] % (int)memory[{}]"
        .format(hex(operators[0]), hex(operators[1]))),
    0x10:
    vm_instr(name="INSTR_OP10",
             instr_size=5,
             stackcost=-2,
             func=lambda operators:
             "memory[OP] = (int)memory[{}] >> (int)memory[{}]".format(
                 hex(operators[0]), hex(operators[1]))),
    0x11:
    vm_instr(
        name="INSTR_OP11",
        instr_size=5,
        stackcost=-2,
        func=lambda operators: "memory[OP] = (int)memory[{}] - (int)memory[{}]"
        .format(hex(operators[0]), hex(operators[1]))),
    0x12:
    vm_instr(name="INSTR_OP12",
             instr_size=5,
             stackcost=-2,
             func=lambda operators:
             "memory[OP] = (int)memory[{}] << (int)memory[{}]".format(
                 hex(operators[0]), hex(operators[1]))),
    0x13:
    vm_instr(
        name="INSTR_OP13",
        instr_size=5,
        stackcost=-2,
        func=lambda operators: "memory[OP] = (int)memory[{}] | (int)memory[{}]"
        .format(hex(operators[0]), hex(operators[1]))),
    0x14:
    vm_instr(
        name="INSTR_OP14",
        instr_size=5,
        stackcost=-1,
        func=lambda operators: "memory[OP] = memory[{}]".format(hex(operators[0]))),
    0x15:
    vm_instr(name="INSTR_OP15",
             instr_size=1,
             stackcost=-2,
             func=lambda operators: "[BYTE* memory[{}]] = memory[{}]".format(
                 hex(operators[1]), hex(operators[0]))),
    0x16:
    vm_instr(name="INSTR_OP16",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[OP] = (unsigned int*)memory[{}]".
             format(hex(operators[0]))),
    0x17:
    vm_instr(
        name="INSTR_OP17",
        instr_size=5,
        stackcost=-2,
        func=lambda operators: "memory[OP] = (int)memory[{}] * (int)memory[{}]"
        .format(hex(operators[0]), hex(operators[1]))),
    0x18:
    vm_instr(
        name="INSTR_OP18",
        instr_size=5,
        stackcost=-2,
        func=lambda operators: "memory[OP] = (int)memory[{}] & (int)memory[{}]"
        .format(hex(operators[0]), hex(operators[1]))),
    0x19:
    vm_instr(name="INSTR_OP19",
             instr_size=5,
             stackcost=-2,
             func=lambda operators:
             "memory[OP] = (int)memory[{}] >> (int)memory[{}]".format(
                 hex(operators[0]), hex(operators[1]))),
    0x1a:
    vm_instr(name="INSTR_OP1A",
             instr_size=5,
             stackcost=-3,
             func=lambda operators: "memory[OP] = 4 * memory[{}] + 64 * memory[{}] + memory[{}]".format(
                 hex(operators[2]), hex(operators[1]), hex(operators[0]))),
    0x1b:
    vm_instr(name="INSTR_OP1B",
             instr_size=1,
             stackcost=-2,
             func=lambda operators: "function1(memory[{}], memory[{}])".format(
                 hex(operators[0]), hex(operators[1]))),
    0x1c:
    vm_instr(name="INSTR_OP1C",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[OP] = (unsigned int*)memory[{}]".
             format(hex(operators[0]))),
    0x1d:
    vm_instr(name="INSTR_OP1D",
             instr_size=5,
             stackcost=-2,
             func=lambda operators: "memory[OP] = Sbox[memory[{}]][memory[{}]]"
             .format(hex(operators[0]), hex(operators[1]))),
    0x1e:
    vm_instr(name="INSTR_OP1E",
             instr_size=1,
             stackcost=-2,
             func=lambda operators: "[QWORD* memory[{}]] = memory[{}]".format(
                 hex(operators[1]), hex(operators[0]))),
    0x1f:
    vm_instr(name="INSTR_OP1F",
             instr_size=1,
             stackcost=-2,
             func=lambda operators: "[QWORD* memory[{}]] = memory[{}]".format(
                 hex(operators[1]), hex(operators[0]))),
    0x20:
    vm_instr(name="INSTR_OP20",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[OP] = [unsigned int* memory[{}]]".
             format(hex(operators[0]))),
    0x21:
    vm_instr(name="INSTR_OP21",
             instr_size=5,
             stackcost=-2,
             func=lambda operators: "memory[OP] = 4 * memory[{}] + memory[{}]".
             format(hex(operators[1]), hex(operators[0]))),
    0x22:
    vm_instr(name="INSTR_OP22",
             instr_size=5,
             stackcost=-2,
             func=lambda operators:
             "memory[OP] = weights[ 256 * memory[{}] + 8 * memory[{}] ]".
             format(hex(operators[0]), hex(operators[1]))),
    0x23:
    vm_instr(name="INSTR_OP23",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[OP] = ..[unsigned int* memory[{}]]"
             .format(hex(operators[0]))),
    0x24:
    vm_instr(name="INSTR_OP24",
             instr_size=5,
             stackcost=-2,
             func=lambda operators:
             "memory[OP] = (QWORD)memory[{}] * (QWORD)memory[{}]".format(
                 hex(operators[0]), hex(operators[1]))),
    0x25:
    vm_instr(name="INSTR_OP25",
             instr_size=5,
             stackcost=-2,
             func=lambda operators:
             "memory[OP] = (char*)memory[{}] + (QWORD)memory[{}]".format(
                 hex(operators[0]), hex(operators[1]))),
    0x26:
    vm_instr(name="INSTR_OP26",
             instr_size=5,
             stackcost=0,
             func=lambda operators: "memory[OP] = mod/*97A95E7981*/"),
    0x27:
    vm_instr(name="INSTR_OP27",
             instr_size=5,
             stackcost=-2,
             func=lambda operators:
             "memory[OP] = (int)memory[{}] % (QWORD)memory[{}]".format(
                 hex(operators[0]), hex(operators[1]))),
    0x28:
    vm_instr(name="INSTR_OP28",
             instr_size=5,
             stackcost=-2,
             func=lambda operators:
             "memory[OP] = sums[ 64 * memory[{}]  + 8 * memory[{}]]".format(
                 hex(operators[0]), hex(operators[1]))),
    0x29:
    vm_instr(name="INSTR_OP29",
             instr_size=5,
             stackcost=-2,
             func=lambda operators: "memory[OP] = memory[{}] !=  memory[{}]".
             format(hex(operators[0]), hex(operators[1]))),
    0x2a:
    vm_instr(name="INSTR_OP2A",
             instr_size=1,
             stackcost=-2,
             func=lambda operators: "memory[{}] = memory[{}] & 1".format(
                 hex(operators[1]), hex(operators[0]))),
    0x2b:
    vm_instr(name="INSTR_OP2B",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[OP] = memory[{}] & 1".format(
                 hex(operators[0]))),
    0x2c:
    vm_instr(name="INSTR_OP2C",
             instr_size=1,
             stackcost=-1,
             func=lambda operators: "return memory[{}]".format(hex(operators[0]))),
    0x2d:
    vm_instr(name="INSTR_OP2D",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[OP] = [int* memory[{}]]".format(
                 hex(operators[0]))),
    0x2e:
    vm_instr(name="INSTR_OP2E",
             instr_size=5,
             stackcost=-2,
             func=lambda operators: "memory[OP] = memory[{}] < memory[{}]".
             format(hex(operators[0]), hex(operators[1]))),
    0x2f:
    vm_instr(name="INSTR_OP2F",
             instr_size=5,
             stackcost=1,
             func=lambda operators: "PUSH OP"),
    0x30:
    vm_instr(name="INSTR_OP30",
             instr_size=2,
             stackcost=-1,
             func=lambda operators: "memory[{}] = OP".format(hex(operators[0]))),
    0x31:
    vm_instr(name="INSTR_OP31",
             instr_size=3,
             stackcost=-1,
             func=lambda operators: "memory[{}] = OP".format(hex(operators[0]))),
    0x32:
    vm_instr(name="INSTR_OP32",
             instr_size=5,
             stackcost=-1,
             func=lambda operators: "memory[{}] = OP".format(hex(operators[0]))),
    0x33:
    vm_instr(name="INSTR_OP32",
             instr_size=9,
             stackcost=-1,
             func=lambda operators: "memory[{}] = OP".format(hex(operators[0]))),
}

cursor = 0
index = 0

our_stack = []
check_stack = []
udi = {}
lim = 38

def u8(s):
    return struct.unpack('<B', s)[0]
def u16(s):
    return struct.unpack('<H', s)[0]
def u32(s):
    return struct.unpack('<I', s)[0]
def u64(s):
    return struct.unpack('<Q', s)[0]

lines = []

while cursor < len(code):
    opcode = code[cursor]
    if opcode not in opcode_tbl.keys():
        print("[!!!] opcode {} at offset {} not found".format(
            opcode, hex(cursor)))
        cursor += 1
        continue

    instr = opcode_tbl[opcode]

    operator = b""
    if instr.instr_size > 1:
        operator = code[cursor + 1:cursor + instr.instr_size]

    # take care jump
    if opcode == 0x04:  # JUMP
        operator_val = u32(operator)
        target_val = cursor + instr.instr_size + 1 + operator_val
        target_val &= 0xffffffff
        instr.pack(our_stack[instr.stackcost:])
        for k, v in udi.items():
            instr.comment = instr.comment.replace(k, v)
        #instr.comment.replace('if (0x1)', '')
        lines.append((cursor, instr.comment, target_val))
        udi = {} # block reach
        our_stack = our_stack[:instr.stackcost]
    else:
        if opcode == 0x2f:  # STACK operation
            operator_val = u32(operator)
            our_stack.append(operator_val)
            instr.pack([]) # instr.comment.replace("OP", hex(operator_val))
            lines.append((cursor, None, None))
            # if cursor > 0x1c32 and cursor < 0x1c3c:
            #     print(hex(operator_val))
        else:
            instr.pack(our_stack[instr.stackcost:])
            # if cursor == 0x1c32 or cursor == 0x1c3c:
            #     print(hex(cursor), instr.comment, hex(our_stack[instr.stackcost:][-1]), operator)
            if instr.instr_size > 1:
                # has OP
                remain_size = instr.instr_size - 1
                if remain_size == 1:
                    operator_val = u8(operator)
                elif remain_size == 2:
                    operator_val = u16(operator)
                elif remain_size == 4:
                    operator_val = u32(operator)
                elif remain_size == 8:
                    operator_val = u64(operator)
                instr.comment = instr.comment.replace("OP", hex(operator_val))
            #if 
            # if cursor == 0x1c32 or cursor == 0x1c3c:
            #     print(hex(cursor), instr.comment)
            ud = ''
            if ' = ' in instr.comment:
                ud, instr.comment = instr.comment.split(' = ', maxsplit=1)
                ud += ' = '
            ori = instr.comment
            ss = re.findall(r'memory\[[0-9a-fA-Fx]+\]', instr.comment)
            rt = re.split(r'memory\[[0-9a-fA-Fx]+\]', instr.comment)
            u = rt[0]
            rt = rt[1:]
            for s, r in zip(ss, rt):
                if s in udi:
                    s = udi[s]
                u += s + r
            instr.comment = u
            instr.comment = ud + instr.comment
            if instr.comment.startswith('memory[') and '] = ' in instr.comment:
                l, r = instr.comment.split(' = ', maxsplit=1)
                if ' ' in r and not(r.startswith('[') and r.endswith(']')) and not(r.startswith('(') and r.endswith(')')):
                    r = '('+r+')'
                assert re.fullmatch(r'0x[0-9a-fA-F]+', l[len('memory['):-1])
                que = [l]
                while len(que) > 0:
                    fr = que[0]
                    que = que[1:]
                    for k, v in list(udi.items()):
                        if fr in v:
                            # print(11, v)
                            del udi[k]
                            que.append(k)
                if len(r) < lim and l not in r:
                    udi[l] = r
                elif l in udi:
                    del udi[l]
            lines.append((cursor, instr.comment, None))
            our_stack = our_stack[:instr.stackcost]

    cursor += instr.instr_size
    index += 1

# CF Rebuild
lm = dict() # key -> goto result
rm = dict() # gotores -> key
cc_map = dict() # cursor -> index
for i, v in enumerate(lines):
    cursor = v[0]
    cc_map[cursor] = i
def next_op(idx, passNone = True):
    idx += 1
    while passNone and idx < len(lines) and lines[idx][1] == None == lines[idx][2]:
        idx += 1
    if idx >= len(lines):
        return None
    return lines[idx]
def trace_execution(key):
    if key in lm:
        return lm[key]
    pc = 0x45
    while pc in range(0x45, 0xef+1) or pc in range(0x1eae, 0x3000):
        cursor, code, target_val = lines[cc_map[pc]]
        if code == 'if (0x1)':
            pc = target_val
            continue
        pc_1 = lines[cc_map[pc] + 1][0]
        if target_val is None:
            pc = pc_1
            continue
        if code.startswith('if (([int* memory[0x1b3]] < 0x') and code.endswith('))'):
            cp = code[len('if (([int* memory[0x1b3]] < '):-2]
            cp = int(cp, 16)
            if key < cp:
                pc = target_val
            else:
                pc = pc_1
            continue
        print(code)
        assert False
    lm[key] = pc
    if pc in rm:
        print('dup', hex(key), hex(rm[pc]), hex(pc))
    else:
        rm[pc] = key
    return pc

for i, (cursor, code, target_val) in enumerate(lines):
    if code is None:
        continue
    nn = next_op(i)
    if nn is not None and nn[0] == 0x45:
        if code.startswith('memory[0x1b3] = (unsigned int*) '):
            ll = code[len('memory[0x1b3] = (unsigned int*) '):]
            ll = int(ll, 16)
            tt = trace_execution(ll)
            code = 'if (0x1)'
            target_val = tt
            lines[i] = cursor, code, target_val

t1b3 = None
t1bb = None
for i, (cursor, code, target_val) in enumerate(lines):
    if code is None:
        continue
    if code.startswith('memory[0x1b3] = '):
        t1b3 = code[len('memory[0x1b3] = '):]
    if code.startswith('memory[0x1bb] = '):
        t1bb = code[len('memory[0x1bb] = '):]
    if target_val is not None:
        if target_val in range(0x46, 0xef+1):
            assert t1b3 is not None
            assert t1b3.startswith('(unsigned int*) ')
            assert code == 'if (0x1)'
            cc = t1b3[len('(unsigned int*) '):]
            if cc.startswith('0x'):
                bv = int(cc, 16)
                target_val = trace_execution(bv)
                lines[i] = cursor, code, target_val
            else:
                assert t1bb is not None
                cond, rv = t1bb.split(' ? ', maxsplit=1)
                bv1, bv2 = rv.split(' : ', maxsplit=1)
                if ' // ' in bv2:
                    bv2 = bv2.split(' // ')[0]
                bv1 = int(bv1, 16)
                bv2 = int(bv2, 16)
                lines[i - 1] = lines[i-1][0], f'if ({cond})', trace_execution(bv1)
                lines[i] = cursor, code, trace_execution(bv2)
            t1b3 = None
            t1bb = None

# DEAD CODE ERASE
visited = set()
def dfs_dde(cur):
    if cur in visited:
        return
    visited.add(cur)
    idx = cc_map[cur]
    cursor, code, target_val = lines[idx]
    pc_l = None
    if idx + 1 < len(lines):
        pc_l = lines[idx + 1][0]
    if target_val is not None:
        dfs_dde(target_val)
        if code == 'if (0x1)':
            return
    elif code is not None and code.startswith('return '):
        return
    if pc_l is not None:
        dfs_dde(pc_l)
dfs_dde(lines[0][0])
for i, (cursor, code, target_val) in enumerate(lines):
    if cursor not in visited:
        lines[i] = cursor, None, None

# JUNK JUMP ERASE
for i, (cursor, code, target_val) in enumerate(lines):
    if code == 'if (0x1)' and (i+1<len(lines) and lines[i+1][0]==target_val) or (next_op(i) is not None and next_op(i)[0] == target_val):
        code = None
        target_val = None
        lines[i] = cursor, code, target_val

# JUMP TARGET Analysis
goto_target = {}
for cursor, code, target_val in lines:
    if target_val is None:
        continue
    if target_val not in goto_target:
        goto_target[target_val] = []
    goto_target[target_val].append(cursor)

# LIVE VAR ANA
dd = True
while dd: # lazy
    AUX = [] # (used, mem_idx or None, is alive, blk_st, blk_end)
    block_start = True
    for i, (cursor, code, target_val) in enumerate(lines):
        if cursor in goto_target:
            block_start = True
        if code is None:
            if block_start and len(AUX) > 1:
                AUX[-1][-1] = True
            AUX.append([[], None, None, block_start, False])
            continue
        mem_idx = None
        alive = None
        if code.startswith('memory[') and '] = ' in code:
            l, r = code.split(' = ', maxsplit=1)
            assert re.fullmatch(r'0x[0-9a-fA-F]+', l[len('memory['):-1])
            mem_idx = int(l[len('memory['):-1], 16)
            alive = False
        else:
            r = code
        mts = re.findall(r'memory\[[0-9a-fA-Fx]+\]', r)
        used = []
        for v in mts:
            t = v[len('memory['):-1]
            assert t.startswith('0x')
            v = int(t, 16)
            used.append(v)
        #lines[i] = (cursor, code + ' // alive ' + ', '.join(map(hex, used)), target_val)
        if block_start and len(AUX) > 1:
            AUX[-1][-1] = True
        AUX.append([used, mem_idx, alive, block_start, False])
        block_start = False
        if target_val is not None:
            block_start = True

    AUX[-1][-1] = True
    mem = {}
    setted = set()
    reqed = set()
    blk_st_cc = None
    blocks = {}
    for i, (cursor, code, target_val) in enumerate(lines):
        used, mem_idx, alive, blk_st, blk_end = AUX[i]
        if blk_st:
            mem = {}
            setted = set()
            reqed = set()
            blk_st_cc = cursor
        for v in used:
            if v not in setted:
                reqed.add(v)
            if v in mem:
                pid = mem[v]
                del mem[v]
                AUX[pid][2] = True
        if mem_idx is not None:
            mem[mem_idx] = i
            setted.add(mem_idx)
        if blk_end:
            nxt_blk = []
            if i + 1 < len(lines):
                nxt_blk.append(lines[i+1][0])
            if target_val is not None:
                if code == "if (0x1)":
                    nxt_blk = []
                nxt_blk.append(target_val)
            assert blk_st_cc is not None
            blocks[blk_st_cc] = [list(reqed), mem, list(setted), nxt_blk]
            # for k, v in mem.items():
            #     print(AUX[v][2])
            #     AUX[v][2] = True

    visited = set()
    def dfs_LVA(cur, ff):
        if cur in visited:
            return
        if len(ff) == 0:
            return
        visited.add(cur)
        reqed, mem, setted, nxt_blk = blocks[cur]
        for v in reqed:
            if v in ff:
                # print(hex(v), hex(ff[v]), AUX[ff[v]][2])
                AUX[ff[v]][2] = True
                del ff[v]
        goon = ff.copy()
        for v in setted:
            if v in goon:
                del goon[v]
        for nxt in nxt_blk:
            dfs_LVA(nxt, goon)

    # can be faster by Tarjan algo to find SCC, but I'm lazy
    for k, v in blocks.items():
        visited = set()
        reqed, mem, setted, nxt_blk = v
        for nn in nxt_blk:
            dfs_LVA(nn, mem.copy())

    dd = False
    for i, (cursor, code, jp) in enumerate(lines):
        dead = AUX[i][2] is not None and AUX[i][2] == False
        if dead:
            lines[i] = (cursor, None, None)
            dd = True

f = open('out2.c', 'w')
for i, (cursor, code, jp) in enumerate(lines):
    if cursor in goto_target:
        f.write(f'L_{hex(cursor)[2:].zfill(4)}: // from ' + ', '.join([f'R_{hex(fr)[2:].zfill(4)}' for fr in goto_target[cursor]]) + '\n')
    if code is None:
        continue
    if jp is None:
        f.write(f"{code};\n")
    else:
        f.write(f"{code} goto L_{hex(jp)[2:].zfill(4)}; // R_{hex(cursor)[2:].zfill(4)}\n")

f.close()