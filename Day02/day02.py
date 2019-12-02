
# PART 1
def gravity_assist(prog, noun, verb):
  prog[1] = noun
  prog[2] = verb

  i = 0
  while True:
    op = prog[i]
    i1, i2, i3 = prog[i+1], prog[i+2], prog[i+3] 
    if op == 99:
      break
    elif op == 1:
      prog[i3] = prog[i1] + prog[i2]
      i += 4
    elif op == 2:
      prog[i3] = prog[i1] * prog[i2]
      i += 4
    else:
      i += 1
  return prog[0]


with open('input.txt') as f:
  program = [int(x) for x in f.read().split(',')]

print('PART 1:', end=' ')
print(gravity_assist(program.copy(), 12, 2))

# PART 2
done = False
for noun in range (0, 100):
  for verb in range(0, 100):
    if gravity_assist(program.copy(), noun, verb) == 19690720:
      print('PART 2:', end=' ')
      print(100*noun + verb)
      done = True
      break
  if done:
    break




