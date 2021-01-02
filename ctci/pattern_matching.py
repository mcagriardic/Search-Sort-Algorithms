"""
From: Cracking the Coding Interview
Pattern Matching
You are given two strings, pattern and value.
The pattern can only be a and b where as values can be for example
catcatcatgocatgo which matches with aaabab. Write a function which tests
to see if the value matches the pattern.
"""

def find_pattern(cs):
    if len(cs) == 0:
        return ""

    # p -> pattern
    p = [cs[0]]
    # tc -> temporary container
    tc = []
    # mi -> match index
    mi = 0
    for i in range(1, len(cs)):
        if cs[i] == p[mi]:
            tc.append(cs[i])
            mi += 1
            if p == tc:
                return "".join(p)
        elif cs[i] != p[mi]:
            p.append(cs[i])
    return "".join(p)

def count_until_next_dif_elem(p):
    c = 1
    for i in range(1, len(p)):
        if p[i-1] == p[i]:
            c += 1
        else:
            break
    return c

def is_pattern_match(cs, pm):
    s = 0
    while len(cs) > 0:
        p = find_pattern(cs)
        cut = count_until_next_dif_elem(pm)
        if p * cut != cs[s:len(p) * cut]:
            return False
        if len(pm) == 0 and len(p) != 0:
            return False
        pm = pm[cut:]
        cs = cs[len(p) * cut:]
    return True

# tc -> test cases
tc = [
    ("catcatcatgogocat", "aaabba"),
    ("catcatcacar", "aabb"),
    ("catcaxcaca", "aabb")
]

[is_pattern_match(cs, pm) for cs, pm in tc]

"""
>> [True, False, False]
"""