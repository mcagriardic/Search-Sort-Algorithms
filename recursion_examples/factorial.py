# Q1 : Write a recursive implementation of the factorial function.
# Recall that n! = 1 × 2 × … × n, with the special case that 0! = 1.

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
    
factorial(5)