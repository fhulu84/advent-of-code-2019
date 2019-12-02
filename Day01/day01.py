from functools import reduce

<<<<<<< HEAD

def fuel_req(mass):
    return int(mass / 3) - 2


def get_modules():
    with open('input.txt') as f:
        modules = [int(line.rstrip('\n')) for line in f]
    return modules

=======
def fuel_req(mass):
  return int(mass / 3) - 2

def get_modules():
  with open('input.txt') as f:
    modules = [int(line.rstrip('\n')) for line in f]
  return modules
>>>>>>> d82c5d44e96cf9da4c281f2d8a1d53a45fca72af

modules = get_modules()
# modules = [1969, 100756] # Test values

# PART 1
# sum of the fuel requirements for all of the modules on my spacecraft
print('PART 1: ', end='')
<<<<<<< HEAD
print(reduce(lambda acc, m: acc + fuel_req(m), modules, 0))

# PART 2


def fuel_itself_req(mass):
    fuel = fuel_req(mass)
    total = 0

    while fuel > 0:
        total += fuel
        fuel = fuel_req(fuel)

    return total


# sum of the fuel requirements for all of the modules on my spacecraft(including fuel itself)
print('PART 2: ', end='')
print(reduce(lambda acc, m: acc + fuel_itself_req(m), modules, 0))
=======
print(reduce(lambda acc, m: acc + fuel_req(m),modules,0))

# PART 2
def fuel_itself_req(mass):
  fuel = fuel_req(mass)
  total = 0
  
  while fuel > 0:
    total += fuel
    fuel = fuel_req(fuel)

  return total

# sum of the fuel requirements for all of the modules on my spacecraft(including fuel itself)
print('PART 2: ', end='')
print(reduce(lambda acc, m: acc + fuel_itself_req(m),modules,0))







>>>>>>> d82c5d44e96cf9da4c281f2d8a1d53a45fca72af
