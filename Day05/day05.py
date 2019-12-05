# PART 1
def gravity_assist(prog, id):
  i = 0
  while i < len(prog):
    cmd = format(prog[i], '05d')
    op = int(cmd[3:])
    m1 = int(cmd[2])
    m2 = int(cmd[1])
    m3 = int(cmd[0])
    
    if op == 99: # terminate
      break
    elif op == 1: # add
      i1 = prog[i+1] if m1 == 0 else i+1
      i2 = prog[i+2] if m2 == 0 else i+2
      i3 = prog[i+3] if m3 == 0 else i+3
      prog[i3] = prog[i1] + prog[i2]
      i += 4
    elif op == 2: # multiply
      i1 = prog[i+1] if m1 == 0 else i+1
      i2 = prog[i+2] if m2 == 0 else i+2
      i3 = prog[i+3] if m3 == 0 else i+3
      prog[i3] = prog[i1] * prog[i2]
      i += 4
    elif op == 3:
      i1 = prog[i+1] if m1 == 0 else i+1
      prog[i1] = id  # input id
      i += 2
    elif op == 4:
      i1 = prog[i+1] if m1 == 0 else i+1
      print(prog[i1])
      i += 2
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
    elif op == 7: # less than
      i1 = prog[i+1] if m1 == 0 else i+1
      i2 = prog[i+2] if m2 == 0 else i+2
      i3 = prog[i+3] if m3 == 0 else i+3
      if prog[i1] < prog[i2]:
        prog[i3] = 1
      else:
        prog[i3] = 0
      i += 4
    elif op == 8: # equals
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
  return prog[0]

with open('input.txt') as f:
  program = [int(x) for x in f.read().split(',')]

# print('PART 1:', end=' ')
# gravity_assist(program, 1) 
print('PART 2:', end=' ')
gravity_assist(program, 5) 