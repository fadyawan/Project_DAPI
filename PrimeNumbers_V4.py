# Fastest programme, time complexity O(n log long n), with UI
from tkinter import *

def prime_number_list():
  list1 = []
  for x in range(2, 101):
    for y in list1:
      if (x % y) == 0:
        break
    else:
      list1.append(x)
  print(list1)
  return(list1)

def main(master): # The main function to start the UI and initialise the Tkinter Frame for the User to use.
  # Variables to create the Frame to hold all the buttons and labels inside the master Tkinter container.
  frame = LabelFrame(master, padx = 3, pady = 3)
  list1 = prime_number_list()
  text = Label(frame, text = "The prime numbers are below,")
  text.pack()
  frame.pack(fill = BOTH, expand = 1)

  for i in range(len(list1)):
    Label(frame, text = list1[i]).pack()
  
master = Tk() # "master" is the variable to initialise the use of tkinter in the python program.
master.attributes("-fullscreen", True) # This line makes the window fullscreen.
main(master) # Launches the function main, in other words launches the program.
