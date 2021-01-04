"""
From fellow analyst
Assume s is a string of lower case characters
Write a program that prints the longest substring of s in which the 
letters occur in alphabetical order. For example in s = 'azcbobobegghakl'
then your program should print
'Longest substring in alphabetical order is: beggh'
In the case of ties, print the first substring. For example if s = 'abcbcd'
the your program should print
'Longest substring in alphabetical order is: abc'
"""

def longest_alphabetical_ss(cs):
    a = dict((chr(i),i) for i in range(65, 123))

    # mc -> main container
    mc = []
    # tc -> temporary container
    tc = []

    for c in cs:
        if not tc:
            tc.append(c)
        else:
            if a[tc[-1]] <= a[c]:
                tc.append(c)
            else:
                if not mc:
                    mc = tc[:]
                    tc = [c]
                else:
                    if len(mc) < len(tc):
                        mc = tc
                        tc = [c]
    return "".join(mc)

cs = 'azcbobobegghakl'
longest_alphabetical_ss(cs)

"""
>> 'beggh'
"""
