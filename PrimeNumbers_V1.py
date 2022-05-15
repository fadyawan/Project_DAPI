# More memory used, same time complexity
for x in range (2, 101): 
  prime = True
  for y in range(2, x):
    if (x % y) == 0:
        prime = False
        break
  if prime == True:
    print(x)
