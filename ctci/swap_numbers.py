"""
Cracking the Coding Interview
Swap the values of two variables, in place (without the use of a temp variable)
"""

def swap_numbers(n1, n2):
    n1 = n1 - n2
    n2 = n1 + n2
    n1 = n2 - n1

    return n1, n2

swap_numbers(-1, 3)

"""
>> (3, -1)
"""

swap_numbers(150, 20)

"""
>> (20, 150)
"""