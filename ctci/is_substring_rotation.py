"""
From: Cracking the Coding Interview
Assuming that we have a method isSubstring,
that returns true or false depending on whether or not string1 is a substring of string2,
use isSubstring to determine whether or not string2 is a rotation of string1.
Eg "waterbottle" is a rotation of "erbottlewat"
"""

def is_substring_rotation(s, to_check):

	if len(s) != len(to_check):
		return False
	elif len(s) == 0 or len(to_check) == 0:
		return False

	return to_check in s * 2

is_substring_rotation("waterbottle", "erbottlewat")

"""
>> True
"""
