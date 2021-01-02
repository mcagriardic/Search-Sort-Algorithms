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
    
    if len(cs) == 2:
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

# alternative to above find_pattern function
# this one is more concise.
def alternative_find_pattern(cs):
    if len(cs) == 0:
        return []

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
                return p
        elif cs[i] != p[mi]:
            p.append(cs[i])

    return p

def next_pattern_index(cs, p):
    i = 0
    j = 0
    # pc -> pattern count
    pc = 0
    # collects the matched characters that are
    # unable to complete the pattern cycle
    # e.g. catcatca -> ca makes a partial match 
    # with the pattern "cat". We substract the
    # length of this container from the index
    # tch -> temp cycle holder
    tch = []
    while i < len(cs):
        if cs[i] == p[j]:
            tch.append(cs[i])
            i += 1
            j += 1
            if j == len(p):
                pc += 1
                j = 0
                tch = []
        else:
            break

    return i - len(tch), ("".join(p), pc)

def complete_pattern_to_standardised(cp):
    # pd -> pattern dictionary
    pd = {}
    # chr_aidx -> char a idx
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
        if npi == 0:
            acc = csl
        cp.append((pp, pc))
    
    return complete_pattern_to_standardised(cp)

# tcs -> test cases
tcs = [
    ("caccacgogodef", "aabbc"),
    ("catcatcatgogocat", "aaabba"),
    ("catcatcacar", "aabbc"),
    ("catcaxcaca", "abcc"),
    ("cacac", "aab"),
    ("ca", "ab"),
    ("cc", "aa"),
    ("c", "a"),
    ("", ""),
]

[compute_pattern(q) == a for q,a in tcs]

"""
>> [True, True, True, True, True, True, True, True, True]
"""