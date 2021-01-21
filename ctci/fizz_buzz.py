
"""
#https://github.com/thundergolfer/interview-with-python/tree/master/problems/fizz-buzz
Write a program that prints the numbers within a range start to end,
or alternatively returns the values in a list. But for multiples of three print
"Fizz" instead of the number and for the multiples of five print "Buzz". For numbers
which are multiples of both three and five print "FizzBuzz".
The number 33 would be 'Fizz', the number 30 (3 x 5 x 2) would be 'Fizzbuzz'.
fizzbuzz( 10, 18 ) # > "Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz"
# Alternatively
fizzbuzz( 4, 10 ) # > [4, 'Buzz', 6, 7, 8, 'Fizz', 'Buzz']
"""

def fizz_buzz(lo, hi):
    results = []
    for i in range(lo, hi + 1):
        if i % 5 == 0 and i % 3 == 0:
            results.append("FizzBuzz")
        elif i % 5 == 0:
            results.append("Buzz")
        elif i % 3 == 0:
            results.append("Fizz")
        else:
            results.append(i)
    return results

fizz_buzz(10,18)

"""
>> ['Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz']
"""