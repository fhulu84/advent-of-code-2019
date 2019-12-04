
def is_valid(pwd, pair_only):
  p = [int(d) for d in str(pwd)]
  pair_length = 1
  pair_lengths = []
  i = 1
  while i < len(p):
    if p[i-1] > p[i]:
      return False

    if p[i-1] == p[i]:
      pair_length += 1
      if i == len(p)-1:
        pair_lengths.append(pair_length)
    else:
      if pair_length > 1:
        pair_lengths.append(pair_length)
        pair_length = 1
    i += 1
  if pair_only:
    return pair_lengths.count(2) >= 1
  else:
    return len(pair_lengths) > 0
        

start = 147981
end = 691423 + 1
count = 0

for password in range(start, end + 1):
  if is_valid(password, False):
    count += 1
    # print(password)

print('PART 1:', end=' ')
print(count)

count = 0
for password in range(start, end + 1):
  if is_valid(password, True):
    count += 1
    # print(password)

print('PART 2:', end=' ')
print(count)







