"""
Question set 3:
Level 1
With a given integral number n, write a program to generate
a dictionary that contains (i, i*i) such that is an integral
number between 1 and n (both included). and then the program
should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

def problem_3(v):
    return dict((i, i**2) for i in range(1, v + 1))

problem_3(8)

"""
>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

# ==========================================================

"""
Question set 4:
Level 1
Write a program which accepts a sequence of comma-separated
numbers from console and generate a list and a tuple which
contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

def problem_4(l):
    return tuple(e for e in l)

problem_4([1,2,3,4])

"""
>> (1, 2, 3, 4)
"""

# ==========================================================

"""
Question set 7:
Level 2
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""

def problem_7(i, j):
    return [[i*j for j in range(j)] for i in range(i)]

problem_7(3,5)

"""
>> [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""

# ==========================================================

"""
Question set 8:
Level 2
Write a program that accepts a comma separated sequence of words as input and prints the words
in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""

def problem_8(l):
    return sorted(l)

problem_8(["book", "by", "zero", "text"])

"""
>> ['book', 'by', 'text', 'zero']
"""

# ==========================================================

"""
Question set 18:
Level 3
Question:
A website requires the users to input username and password to register. Write a program 
to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords 
and will check them according to the above criteria. Passwords that 
match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""

# p -> password
def check_validity(p):
    if len(p) < 6:
        return False

    if len(p) > 12:
        return False

    CHARACTERS = ["$", "#", "@"]
    cisupper, cislower, cisdigit, cischaracter = tuple(False for i in range(3))
    # c -> char
    for c in p:
        if c.isupper():
            cisupper = True
        elif c.islower():
            cislower = True
        elif c.isdigit():
            cisdigit = True
        elif c in CHARACTERS:
            cischaracter = True

    return all((cisupper, cislower, cisdigit, cischaracter))

# pws -> passwords
def problem_18(pws):
    return [check_validity(p) for p in pws]

problem_18(["ABd1234@1","a F1#","2w3E*","2We3345"])

"""
>> [True, False, False, False]
"""

# ==========================================================

"""
Question set 19:
Level 3
You are required to write a program to sort the (name, age, score) tuples by 
ascending order where name is string, age and height are numbers. The tuples are 
input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), 
('Json', '21', '85'), ('Tom', '19', '80')]
"""

from functools import cmp_to_key

def sort_alphabetically(cs1, cs2):
    i = 0
    short_cs = min(cs1, cs2)
    while i < len(short_cs):
        if ord(cs1[i]) < ord(cs2[i]):
            return -1
        elif ord(cs1[i]) > ord(cs2[i]):
            return 1
        i += 1
    return 0

def sort_by_score(t1, t2):
    t1n, t1a, t1s = t1
    t2n, t2a, t2s = t2
    if t1s > t2s:
        return 1
    elif t1s < t2s:
        return -1
    else:
        return 0

def sort_by_age(t1, t2):
    t1n, t1a, t1s = t1
    t2n, t2a, t2s = t2
    if t1a > t2a:
        return 1
    elif t1a < t2a:
        return -1
    else:
        return sort_by_score(t1, t2)

def sort(t1, t2):
    t1n, t1a, t1s = t1
    t2n, t2a, t2s = t2
    # if t1 comes before t2
    if sort_alphabetically(t1n, t2n) == -1:
        return 1
    #if t2 comes before t1
    elif sort_alphabetically(t1n, t2n) == 1:
        return -1
    # t1 and t2 are the same character set
    else:
        return sort_by_age(t1, t2)

def problem_19(l):
    return sorted(l, key=cmp_to_key(sort))

problem_19(
    [
        ('John', '20', '90'),
        ('Tom',  '19', '80'),
        ('Jony', '17', '91'),
        ('Jony', '17', '93'),
        ('Json', '21', '85')
    ]
)

"""
>> [('John', '20', '90'),
>>  ('Jony', '17', '93'),
>>  ('Jony', '17', '91'),
>>  ('Json', '21', '85'),
>>  ('Tom', '19', '80')]
"""

# ==========================================================

"""
Question set 20:
Level 3
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.
"""

class Iterable7:
    def __init__(self, v):
        # v -> value
        self.v = v
        # s -> start
        self.s = 1
    
    def __iter__(self):
        while self.s <= self.v:
            if self.s % 7 == 0:
                yield self.s
            self.s+=1

[ch for ch in Iterable7(14)]

"""
>> [7, 14]
"""

# ==========================================================

"""
Question 22
Level 3
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
"New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""

from collections import defaultdict

# inefficient solution
def get_word_counts(s):
    s = s.split(" ")
    return {w: s.count(w) for w in s}

# efficient solution
def get_word_counts(s):
    s = s.split(" ")
    d = defaultdict(lambda: 0)
    for w in s:
        d[w] += 1
    return d

s = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3." 
get_word_counts(s)

"""
>> defaultdict(<function __main__.<lambda>()>,
            {'New': 1,
             'to': 1,
             'Python': 5,
             'or': 2,
             'choosing': 1,
             'between': 1,
             '2': 2,
             'and': 1,
             '3?': 1,
             'Read': 1,
             '3.': 1})
"""

# ==========================================================

"""
Question 12
Level 2
Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

def get_even():
    return ",".join([str(i) for i in range(1000, 3001) if i % 2 == 0])

get_even()