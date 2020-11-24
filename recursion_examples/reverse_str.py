# Q3: Write a recursive function that, given a
# string s, prints the characters of s in reverse order.

def reverse_str(cs):
    if len(cs) == 0:
        return cs
    
    return cs[-1] + reverse_str(cs[0:-1])

reverse_str("abcd")