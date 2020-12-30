"""
Inspired by: https://www.hackerrank.com/challenges/validating-postalcode/problem (removed regex criteria)

Validate postcodes

A valid postal code P have to fulfil both below requirements:

P must be a number in the range from 100000 to 999999 inclusive.
P must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit.
In other words, an alternating repetitive digit pair is formed by
two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

Return True (for valid) while postcode is between 100000 and 999999,
and there are no alternating digits
Return False for invalid
"""
