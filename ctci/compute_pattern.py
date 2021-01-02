"""
Compute the pattern of a given string in a standardised form
E.g.:

cs1 = "caccacgogodef" -> "aabbc"
cs2 = "caccacgogocaccacgo" -> "aabbaab"

"""

# cs -> character set
def find_pattern(cs):
    if len(cs) == 1:
        return [cs]
    
    if cs[0] == cs[1]:
        return [cs[0]]
    
    # p -> pattern
    p = []
    for i in range(1, len(cs)):
        if not p or len(p) == 1:
            p.append(cs[i-1])
            continue
        else:
            if (
                cs[i-1] == p[0]
                and
                cs[i] == p[1]
            ):
                return p
            else:
                p.append(cs[i-1])

    if i + 1 == len(cs):
        p.append(cs[i])
    
    return p

def ALTERNATIVE_FIND_PATTERN(cs):
    if len(cs) == 0:
    return []

    tc1 = [cs[0]]
    tc2 = []
    mi = 0
    for i in range(1, len(cs)):
        if cs[i] == tc1[mi]:
            tc2.append(cs[i])
            mi += 1
            if tc1 == tc2:
                return tc1
        elif cs[i] != tc1[mi]:
            tc1.append(cs[i])

    return tc1

def next_pattern_index(cs, p):
    i = 0
    j = 0
    # pc -> pattern count
    pc = 0
    while i < len(cs):
        if cs[i] == p[j]:
            i += 1
            j += 1
            if j == len(p):
                pc += 1
                j = 0
        else:
            break
    return i, ("".join(p), pc)

def complete_pattern_to_standardised(cp):
    # pd -> pattern dictionary
    pd = {}
    # -> char a idx
    chr_aidx = 97
    for k,_ in cp:
        if k not in pd:
            pd[k] = chr(chr_aidx)
            chr_aidx += 1
    
    pattern = ""
    # p -> pattern, oc -> occurrence count
    for p, oc in cp:
        pattern += pd[p] * oc
    
    return pattern
    
def compute_pattern(cs):
    # cp - > complete pattern
    cp = []
    # npi -> next pattern index
    npi = 0
    # csl -> char set len
    csl = len(cs)
    # acc -> accumulator
    acc = 0
    while acc < len(cs):
        p = find_pattern(cs[acc:csl])
        # pp -> pattern prev, pc -> pattern count
        npi, (pp, pc) = next_pattern_index(cs[acc:csl], p)
        acc += npi
        cp.append((pp, pc))
        
    return complete_pattern_to_standardised(cp)

cs1 = "caccacgogodef"
cs2 = "caccacgogocaccacgo"

[compute_pattern(c) for c in [cs1, cs2]]

"""
>> ['aabbc', 'aabbaab']
"""