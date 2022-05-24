# More memory used, same time complexity
for x in range (0, 101):        # To iterate through every single number from 0 to 100.
  if x >= 2:                    # Checking if a number is above 2 since 2 is the first prime number.
    prime = True                # Setting boolean flag called prime to true, this makes our assumption that the number we are checking is a prime number.
    for y in range(2, x):       # Setting a divisor from two, because dividing by 0 is 0, and dividing by 1 doesn't return any of the values.
      if (x % y) == 0:          # Modulus function to check the remainder of the division, if it is 0, that means it is divisible by a number other than itself or one.
          prime = False         # Since the number is now proven to not be a prime number, we can set the flag as false.
          break                 # Leaving the if statement and iterating to the next x value.
    if prime == True:           # If prime is still true because the if statement above doesn't break, we can print x since we know it is a prime number.
      print(x)                  # Printing x
