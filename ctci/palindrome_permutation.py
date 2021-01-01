"""
From: Cracking the Coding Interview
Check if a string is a permutation of a palindrome.
Palindrome is defines as a string which is the same backwards as it is forwards (taco cat, madam)
Permutation is the letters in the string scrambled.
"""

from collections import defaultdict

def is_palindrome_permutation(s):
    s = s.split(" ")
    s1, s2 = s[0], s[1]

    d2 = defaultdict(lambda: 0)
    for c2 in s2:
        d2[c2] += 1

    for c1 in s1:
        if c1 in d2:
            d2[c1] -= 1

    return sum(d2.values()) == 0

is_palindrome_permutation("taco cat")

"""
>> True
"""

is_palindrome_permutation("taco catx")

"""
>> False
"""