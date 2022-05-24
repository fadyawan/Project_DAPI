# with UI
from tkinter import *

# Generating the list of prime numbers
def prime_number_list():
  l2 = []                               # Creating a list to store found prime numbers.
  for x in range(0, 101):               # To iterate through every single number from 0 to 100.
    if x >= 2:                          # Checking if a number is above 2 since 2 is the first prime number.
      for y in l2:                      # Selecting a divisor from the list of prime numbers
        if (x % y) == 0:                # Modulus function to check the remainder of the division, if it is 0, that means it is divisible by a number other than itself or one.
          break                         # Leaving the if statement and iterating to the next x value.
      else:                             # Else statement for when the conditions of a not prime number are not met, therefore we know it is a prime number.
        l2.append(x)                    # So we append it onto the list.
  print(l2)                             # Printing the list l2.
  return l2                             # Returning the list so that there is a result when the function is executed.

# The main function to start the UI and initialise the Tkinter Frame for the User to use.
def main(master):
  frame = LabelFrame(master, padx = 3, pady = 3)  # Variables to create the Frame to hold all the buttons and labels inside the master Tkinter container.
  list1 = prime_number_list()
  print(list1)
  text = Label(frame, text = "The prime numbers are below,")
  text.pack()
  frame.pack(fill = BOTH, expand = 1)

  for i in range(len(list1)):
    Label(frame, text = list1[i]).pack()
  
master = Tk()                           # "master" is the variable to initialise the use of tkinter in the python program.
master.attributes("-fullscreen", True)  # This line makes the window fullscreen.
main(master)                            # Launches the function main, in other words launches the program.
