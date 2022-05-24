# Fastest programme, time complexity O(n log long n)
l2 = [] # Creating a list to store found prime numbers.
for x in range(0, 101): # To iterate through every single number from 0 to 100.
  if x >= 2: # Checking if a number is above 2 since 2 is the first prime number.
    for y in l2: # Selecting a divisor from the list of prime numbers
      if (x % y) == 0:  # Modulus function to check the remainder of the division, if it is 0, that means it is divisible by a number other than itself or one.
        break # Leaving the if statement and iterating to the next x value.
    else: # Else statement for when the conditions of a not prime number are not met, therefore we know it is a prime number.
      l2.append(x) # So we append it onto the list.
print(l2) # Printing the list l2.
