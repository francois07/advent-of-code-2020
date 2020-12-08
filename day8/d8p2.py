input = [x for x in open('input.txt', 'r').read().splitlines()]


def parse_instructions(data):
    return [(line.split(" ")[0], int(line.split(" ")[1])) for line in data]


def find_loop(ins):
    a = []
    acc = 0
    i = 0
    while i < len(ins):
        a.append(i)
        last_idx = i
        if ins[i][0] == "acc":
            acc += ins[i][1]
            i += 1
        elif ins[i][0] == "jmp":
            i += ins[i][1]
        elif ins[i][0] == "nop":
            i += 1
        if i in a:
            return (acc, last_idx)
    return (acc, -1)


def fix_loop(ins):
    jmp = [(ins[x], x)
           for x in range(len(ins)) if ins[x][0] == "jmp"]
    nop = [(ins[x], x)
           for x in range(len(ins)) if ins[x][0] == "nop"]
    for i in jmp:
        arr = [ins[x] if x != i[1] else ("nop", ins[x][1])
               for x in range(len(ins))]
        loop = find_loop(arr)
        if loop[1] == -1:
            return loop
    for i in nop:
        arr = [ins[x] if x != i[1] else ("jmp", ins[x][1])
               for x in range(len(ins))]
        loop = find_loop(arr)
        if loop[1] == -1:
            return loop
    return -1


print(fix_loop(parse_instructions(input)))
