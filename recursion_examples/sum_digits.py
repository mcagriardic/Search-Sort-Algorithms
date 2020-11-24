# Q2: Write a recursive function that, given a number
# n, returns the sum of the digits of the number n.

import math

def sum_digits(n):
    sd = 0
    if n < 10:
        return n
    
    sd += n % 10
    return sd + sum_digits(math.floor(n/10)) 

sum_digits(155)