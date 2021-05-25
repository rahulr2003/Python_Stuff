"""
Count the number of integers in list formed below starting with 1,2,3,4,5,6,7,8 and 9 respectively.

Use Minimal lines of code to make the program efficient.

A part of the program has already been written below.
"""

import secrets # Module for generating random numbers
list1 = [] # initialising a list
for i in range(0,1000000): # using a loop to input random numbers into list1
	list1.append(secrets.randbelow(1000000000)
