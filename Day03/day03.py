# PART 1
# get points visited as path
def path(moves):
  x = 0
  y = 0
  # points = set()
  points = []
  for move in moves:
    d = move[0] # direction(Right, Left, Up, Down)
    length = int(move[1:]) # length of move  e.g. R5
    
    for _ in range(0, length):
      if d == 'R':
        x += 1
      elif d == 'L':
        x -= 1
      elif d == 'U':
        y += 1
      elif d == 'D':
        y -= 1
      points.append((x,y))
    
  return points

def manhattan_dist(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

with open('input.txt') as f:
  wire1 = f.readline().rstrip('\n').split(',')
  wire2 = f.readline().rstrip('\n').split(',')
  
path1 = path(wire1)
path2 = path(wire2)
# print(path1)
# print(path2)

intersections = list(set(path1).intersection(set(path2)))
# print(intersections)

distances = [manhattan_dist(p1, (0,0)) for p1 in intersections]
# print(distances)

print('PART 1:', end=' ')
print(min(distances))

# PART 2
# total steps taken to reach intersections
total_steps = [path1.index(p)+1+path2.index(p)+1 for p in intersections] 

print('PART 2:', end=' ')
print(min(total_steps))



      



