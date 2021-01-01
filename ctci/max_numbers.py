"""
Cracking the Coding Interview
Write a method which finds the two max numbers in a list/series of numbers.
Locate the numbers without using if/else statements, or any other comparing methods.
"""

def get_two_biggest_num(l):
	return sorted(l)[-2:]

get_two_biggest_num([1,4,3,2,6,8,10])

"""
>> [8, 10]
"""