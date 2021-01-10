"""
From: Cracking the Coding Interview
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string.
"""

def compress_me(cs):
    cs = "".join((cs, " "))
    compressed = []
    count = 1
    for i in range(1, len(cs)):
        if cs[i - 1] != cs[i]:
            compressed.extend([cs[i - 1], str(count) if count != 1 else ""])
            count = 1
            continue
        count += 1

    return "".join(compressed)

compress_me("aaaabbbbccddaa")

"""
>> 'a4b4c2d2a2'
"""

compress_me("abcdeee")

"""
>> 'abcde3'
"""