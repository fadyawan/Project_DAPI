# Less memory used, same time complexity
for x in range (2, 101): 
    for y in range(2, x):
      if (x % y) == 0:
        break 
    else:    #For, Else is a thing, If it doesn't break it goes to Else, if it breaks it iterates through to the first for loop.
      print(x)
