# Fastest programme, time complexity O(n log long n)
l2 = []
for x in range(2, 101):
  for y in l2:
    if (x % y) == 0:
      break
  else:
    l2.append(x)
print(l2)
