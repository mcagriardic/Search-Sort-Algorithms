"""
From: https://www.hackerrank.com/challenges/no-idea/problem
There is an array of  integers. There are also 2 disjoint sets, A and B , each m containing  integers.
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
For each i integer in the array, if i in A, you add 1 to your happiness. If i in B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.
Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
Input Format:
Accept three strings, first and second is A and B with integers separated by spaces,
third string is the array with integers separated by spaces.
"""

# cs_to_l -> character set to list
# of -> output format
def cs_to_l(cs, of='set'):
    if of == 'set':
      return {int(e) for e in cs.split(" ")}
    return [int(e) for e in cs.split(" ")]

def happiness_assessment(a,b,i):
    a = cs_to_l(a)
    b = cs_to_l(b)
    i = cs_to_l(i, 'l')

    # hs -> happiness score
    hs = 0
    for n in i:
      if n in a:
        hs += 1
      elif n in b:
        hs -= 1
    
    return hs

happiness_assessment(
    '8 9 3 4 5',
    '6 7 1 2',
    '1 5 9 7 2'
)

"""
>> -1
"""