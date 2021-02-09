## Boolean Operators

Used as conjunctions to combine or exclude keywords in a search

#### and | or | not

### order of precedence
0. Evaluate all boolean expressions to booleans
1. not
2. and
3. or

*Ex.*
```python
if (A and B):
  print ("hello")

elif (C or D):
  print ("hi")
```


## Random Number Generator

A Function that let the computer pick a number within a range.


### Formula:
```python
# Import the random library
import random		# Line 1

# Pick a number randomly within a range
variable = random.randint(startNum, endNum)
```

### Rule
In order to set a range, check how many options are needed. In example, a coin flipper has 2 sides, so 2 options.

*Ex. * 
```python
import random

coin = random.randint(0,1)

if (coin == 1):
	print ("head")
else:
	print ("tail")
```
> head *or* tail