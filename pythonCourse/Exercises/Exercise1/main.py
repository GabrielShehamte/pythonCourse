import random
import FreeSimpleGUI as FSG

lower = input("Enter the lower bound: ")
upper = input ("Enter the upper bound: ")
bound = random.randrange(lower, upper)

print("the bound is: " + bound)