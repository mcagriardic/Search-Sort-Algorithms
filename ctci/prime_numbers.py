#https://github.com/mre/the-coding-interview/tree/master/problems/prime-number

"""
Prime Number
Write a function that accepts a number and return a boolean based on whether it's a prime number.
"""

def is_prime_number(val):
    i = 2
    while True:
        if val == i:
            return True
        if val % i == 0:
            return False
        i+= 1