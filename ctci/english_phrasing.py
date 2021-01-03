"""
Cracking the Coding Interview
When given an int, return the int value phrased in English.

Eg
1320
Two Thousand Three Hundred Twenty (no "ands" required)
"""

# ws -> wordset
def english_phrasing(ws):
    dict_nums_1 = {
        "one":   1,
        "two":   2,
        "three": 3,
        "four":  4,
        "five":  5,
        "six":   6,
        "seven": 7,
        "eight": 8,
        "nine":  9,  
    }

    dict_nums_10 = {
        "ten":     10,
        "twenty":  20,
        "thirty":  30,
        "fourty":  40,
        "fifty":   50,
        "sixty":   60,
        "seventy": 70,
        "eighty":  80,
        "ninety":  90
    }

    dict_nums_m = {
        "thousand": 1000,
        "million":  1000000,
        "billion":  1000000000,
    }

    ws = ws.lower().split(" ")

    # acc -> accumulator
    acc = 0
    # tacc -> temporary accumulator
    tacc = 0
    for w in ws:
        if w == "hundred":
            tacc *= 100
        elif w not in dict_nums_m:
            if w in dict_nums_1:
                tacc += dict_nums_1[w]
            elif w in dict_nums_10:
                tacc += dict_nums_10[w]
        else:
            acc = tacc * dict_nums_m[w]
            tacc = 0

    if tacc != 0:
        acc += tacc

    return acc

english_phrasing("Two Hundred Ninety Three Thousand Three Hundred Eighty Four")

"""
>> 293384
"""
