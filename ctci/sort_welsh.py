from functools import cmp_to_key

def generate_dictionary():
    s = "a, b, c, ch, d, dd, e, f, ff, g, ng, h, i, k, l, ll, m, n, o, p, ph, r, rh, s, t, th, u, w, y"
    return dict((l,i) for i,l in enumerate(s.split(", ")))

def numerise_cs(cs):
    num = []
    i = 1
    lang_dict = generate_dictionary()
    while i <= len(cs):
        if i == len(cs):
            num.append(lang_dict[cs[i-1]])
            break
  
        if (cs[i-1] + cs[i]) in lang_dict:
            num.append(lang_dict[(cs[i-1] + cs[i])])
            i += 2 # skip the window
        else:
            num.append(lang_dict[cs[i-1]])
            i += 1
    return num

def sort_welsh(cs1, cs2):
    if len(cs1) < len(cs2):
        return -1
    elif len(cs1) > len(cs2):
        return 1

    for c1, c2 in zip(numerise_cs(cs1), numerise_cs(cs2)):
        if c1 < c2:
            return -1
        elif c1 > c2:
            return 1
    return 0

## Custom sort ##

test_case = ["dda", "fork", "dea", "dda"]

sorted(test_case, key=cmp_to_key(sort_welsh))

"""
>> ['dea', 'dda', 'dda', 'fork']
"""


## Conventional sort ##

# tcc -> test case copy
tcc = test_case[:]
tcc.sort()
tcc

"""
>> ['dda', 'dda', 'dea', 'fork']
"""