steps = 0
c = 10
d = 10
goal = int(input('What step amount do you want to find? '))
while steps < goal:
  product = 1
  steps = 0
  print(c)
  while c > 9:
    for digit in range(0, len(str(c))):
        product *= int(str(c)[digit])
    print(product)
    steps += 1
    c = product
    product = 1
  print("Steps:", steps)
  c *= 0
  d += 1
  c += d