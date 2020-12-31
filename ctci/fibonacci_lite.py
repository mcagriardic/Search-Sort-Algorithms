"""
Hackerrank: https://www.hackerrank.com/contests/programming-interview-questions/challenges/fibonacci-lite
For this question, you will write a program that generates values from the Fibonacci sequence.
The Fibonnaci sequence is recursively defined by:
Fn = Fn - 1 + Fn - 2
Using the following seed values:
F0 = 0, F1 = 1
Given a number n, print the nth value of the Fibonacci sequence.
Examples
Input:
12
Output:
144
Input:
30
Output:
832040
General Approach
Find the base case(s),
Have your function recognize the base case(s) and provide a solution,
Recursively define a solution to the sub-problem for other inputs,
Call your function on the input and print the result to STDOUT.
Things to think about
Although we are doing this mainly to learn recursion, think about whether this is effecient
in your language of choice. Does your language support tail call elimination?
Input Format and Restrictions
Each test case will consist of a single positive integer n.
The inputs will always satisfy the following restrictions:
Fn < 2^32 - 1,
0 <= n < 50
"""

def __fib(a,b,n,c=0):
    if c == n:
        return a
    c += 1
    return __fib(b,a+b,n,c)

def fib(n):
    a = 0
    b = 1
    return __fib(a, b, n)

fib(12)

"""
>> 144
"""

fib(12)

"""
>> 832040
"""