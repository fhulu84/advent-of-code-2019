def find_path(grf, s, e, path =[]): 
  path = path + [s] 
  if s == e: 
    return path 
  
  node = grf[s]
  if node != '':
    if node not in path:
      newpath = find_path(grf, node, e, path) 
      if newpath:  
        return newpath
      return None

with open('input.txt') as f:
  map = [line.rstrip('\n') for line in f]

graph = {
  'COM': ''
}

for r in map:
  o = r.split(')')
  if o[1] not in graph.keys():
    graph[o[1]] = o[0]

# PART 1
total_orbits = 0
for o in graph.keys():
  if o == 'COM':
    continue
  total_orbits += len(find_path(graph, graph[o], 'COM'))

print('PART 1:', end=' ')
print(total_orbits)

# PART 2
you_path = find_path(graph, 'YOU', 'COM')[1:-1]
san_path = find_path(graph, 'SAN', 'COM')[1:-1]

dist = 0
for s in you_path:
  if s in san_path:
    dist = dist + san_path.index(s)
    break
  else:
    dist += 1

print('PART 2:', end=' ')
print(dist)
    





  




