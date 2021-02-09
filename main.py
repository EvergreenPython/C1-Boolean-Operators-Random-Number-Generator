'''
02/08/2021
Boolean Operators
- Used as conjunctions to combine or exclude keywords in a search

A = True
B = False
C = 5 > 3 # True
D = 6 == 4  # False

if (A and B): # True and False >> False
  print ("hello")
 
elif (C or D):  # True or False >> True
  print ("hi")

Truth table

    A     B      A and B     A or B   not A
  True  True      True        True    False   
  True  False     False       True    False
  False True      False       True    True
  False False     False       False   True

print (5 == "five" or not(5 > 1 and not 0 != 0) or False and not 6 >= 6 and 10 <= 11)
print (5 == "five" or not(True and not False) or False and not 6 >= 6 and 10 <= 11)
print (False or not(True and not False) or False and not True and True)
print (False or not(True and True) or False and not True and True)
print (False or not True or False and not True and True)
print (False or False or False and False and True)
print (False or False or False and True)
print (False or False or False)
print (False or False)
print (False)

# Prompt the user to input a year
year = int(input("Enter a year: "))

# Using if statements, output whether the inputted year is or is not a leap year
if (year % 100 == 0 and year % 400 == 0):
  print (str(year) + " is a leap year.")

elif (year % 4 == 0 and year % 100 != 0):
  print (str(year) + " is a leap year.")

else:
  print (str(year) + " is not a leap year.")

=======================================================================

Random Number Generator

import random must be stated any code above.


# Importing Random library
import random

coin = random.randint(0, 1)

# 0 >> heads
if (coin == 0):
  print ("heads")

# 1 >> tails
elif (coin == 1):
  print ("tails")

# Exercise
# Rolling a dice (6sides)
import random

dice = random.randint(1,6)

if (dice == 1):
  print ("You rolled a 1")
elif (dice == 2):
  print ("You rolled a 2")
elif (dice == 3):
  print ("You rolled a 3")
elif (dice == 4):
  print ("You rolled a 4")
elif (dice == 5):
  print ("You rolled a 5")
elif (dice == 2):
  print ("You rolled a 6")

'''
# Exercise: Rock Paper Scissors (RPS)
import random

print ("Welcome to RPS")
print ("1. rock")
print ("2. paper")
print ("3. scissors")
p1 = input("Enter your choice: ")

cpu = random.randint(1,3)

# 1 : rock , 2 : paper , 3 : scissors

# Convert 1
if (p1 == "1" or p1 == "rock"):
  p1 = 1
# Convert 2
elif (p1 == "2" or p1 == "paper"):
  p1 = 2
# Convert 3
elif (p1 == "3" or p1 == "scissors"):
  p1 = 3

# Rock vs Rock  (t)
# Rock vs Paper (l)
# Rock vs Scissors (w)

# Paper vs Rock (w)
# Paper vs Paper  (t)
# Paper vs Scissors (l)

# Scissors vs Rock (l)
# Scissors vs Paper (w)
# Scissors vs Scissors (t)

# Tied
if (p1 == cpu):
  print ("Tied")

# player won
elif (p1 == 1 and cpu == 3 or p1 == 2 and cpu == 1 or p1 == 3 and cpu == 2):
  print ("Player won")

# player lost
elif (p1 == 1 and cpu == 2 or p1 == 2 and cpu == 3 or p1 == 3 and cpu == 1):
  print ("Player lost")

if (cpu == 1):
  print ("cpu : rock")
elif (cpu == 2):
  print ("cpu : paper")
elif (cpu == 3):
  print ("cpu : scissors")