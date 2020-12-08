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


print(find_loop(parse_instructions(input)))
