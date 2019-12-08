# Code needs refactoring!....
from itertools import permutations


class Amplifier:
    def __init__(self, prog, phase, i=0):
        self.prog = prog
        self.inputs = [phase]
        self.i = i

    def get_prog(self):
        return self.prog

    def get_inputs(self):
        return self.inputs

    def get_i(self):
        return self.i

    def set_i(self, value):
        self.i = value


def gravity_assist(prog, ids):
    i = 0
    output = None
    while i < len(prog):
        cmd = format(prog[i], '05d')
        op = int(cmd[3:])
        m1 = int(cmd[2])
        m2 = int(cmd[1])
        m3 = int(cmd[0])

        if op == 99:  # terminate
            break
        elif op == 1:  # add
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            i3 = prog[i+3] if m3 == 0 else i+3
            prog[i3] = prog[i1] + prog[i2]
            i += 4
        elif op == 2:  # multiply
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            i3 = prog[i+3] if m3 == 0 else i+3
            prog[i3] = prog[i1] * prog[i2]
            i += 4
        elif op == 3:
            i1 = prog[i+1] if m1 == 0 else i+1
            prog[i1] = ids.pop(0)  # input id
            i += 2
        elif op == 4:
            i1 = prog[i+1] if m1 == 0 else i+1
            output = prog[i1]
            i += 2
            break
        elif op == 5:  # jump-if-true
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            if prog[i1] != 0:
                i = prog[i2]
            else:
                i += 3
        elif op == 6:  # jump-if-false
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            if prog[i1] == 0:
                i = prog[i2]
            else:
                i += 3
        elif op == 7:  # less than
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            i3 = prog[i+3] if m3 == 0 else i+3
            if prog[i1] < prog[i2]:
                prog[i3] = 1
            else:
                prog[i3] = 0
            i += 4
        elif op == 8:  # equals
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            i3 = prog[i+3] if m3 == 0 else i+3
            if prog[i1] == prog[i2]:
                prog[i3] = 1
            else:
                prog[i3] = 0
            i += 4
        else:
            i += 1
    return output


def intcode_computer(amp):
    prog = amp.get_prog()
    i = amp.get_i()
    output = None
    while i < len(prog):
        cmd = format(prog[i], '05d')
        op = int(cmd[3:])
        m1 = int(cmd[2])
        m2 = int(cmd[1])
        m3 = int(cmd[0])

        if op == 99:  # terminate
            break
        elif op == 1:  # add
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            i3 = prog[i+3] if m3 == 0 else i+3
            prog[i3] = prog[i1] + prog[i2]
            i += 4
        elif op == 2:  # multiply
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            i3 = prog[i+3] if m3 == 0 else i+3
            prog[i3] = prog[i1] * prog[i2]
            i += 4
        elif op == 3:
            i1 = prog[i+1] if m1 == 0 else i+1
            prog[i1] = amp.get_inputs().pop(0)  # input id
            i += 2
        elif op == 4:
            i1 = prog[i+1] if m1 == 0 else i+1
            output = prog[i1]
            i += 2
            break
        elif op == 5:  # jump-if-true
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            if prog[i1] != 0:
                i = prog[i2]
            else:
                i += 3
        elif op == 6:  # jump-if-false
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            if prog[i1] == 0:
                i = prog[i2]
            else:
                i += 3
        elif op == 7:  # less than
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            i3 = prog[i+3] if m3 == 0 else i+3
            if prog[i1] < prog[i2]:
                prog[i3] = 1
            else:
                prog[i3] = 0
            i += 4
        elif op == 8:  # equals
            i1 = prog[i+1] if m1 == 0 else i+1
            i2 = prog[i+2] if m2 == 0 else i+2
            i3 = prog[i+3] if m3 == 0 else i+3
            if prog[i1] == prog[i2]:
                prog[i3] = 1
            else:
                prog[i3] = 0
            i += 4
        else:
            i += 1
    amp.set_i(i)
    return output


with open('input.txt') as f:
    program = [int(x) for x in f.read().split(',')]

max_t_s = None
for p in permutations([0, 1, 2, 3, 4]):
    output = -1
    for i, phase in enumerate(p):
        if i == 0:
            inputs = [phase, 0]
        else:
            inputs = [phase, output]
        output = gravity_assist(program.copy(), inputs)
        max_t_s = max([max_t_s, output]) if max_t_s is not None else output

print('PART 1:', end=' ')
print(max_t_s)

max_t_s = None
output = None
last_out = None

for perm in permutations([5, 6, 7, 8, 9]):
    progs = [Amplifier(program.copy(), p) for p in perm]

    output = 0
    while True:
        if output is None:
            break
        for i in range(5):
            progs[i].get_inputs().append(output)
            output = intcode_computer(progs[i])
        last_out = last_out if output is None else output
    max_t_s = max([max_t_s, last_out]) if max_t_s is not None else last_out


print('PART 2:', end=' ')
print(max_t_s)
