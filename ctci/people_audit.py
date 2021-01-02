"""
Cracking the Coding Interview
Given a list of birth and death pairs between 1900 and 2000 compute
the year most people where alive.
You should count the person on the year of their birth and death,
as well as in between.
"""

import random
from collections import defaultdict

def generate_pairs(sample_size):
    bday = [
        random.randint(1900, 2000)
        for i in range(sample_size)
    ]
    dday = [
        random.randint(bd, 2000)
        for bd in bday
    ]

    return [(bd, dd) for (bd,dd) in zip(bday, dday)]

def get_most_crowded_year(pairs)
	alive_dict = defaultdict(lambda: 0)
	for bd, dd in pairs:
	    for y in range(bd, dd + 1):
	        alive_dict[y] += 1
	return max(alive_dict.items(), key= lambda k: k[1])

sample_size = 250
pairs = generate_pairs(sample_size)
get_most_crowded_year(pairs)

"""
>> (1971, 93)
"""