# Q6: Write a recursive function that, given two strings,
# returns whether the first string is a subsequence of the
# second. For example, given hac and cathartic, you should
# return true, but given bat and table, you should return false.

def is_subsequence(
    cs1,
    cs2,
):
    if len(cs1) == 0:
        return True

    if len(cs2) == 0:
        return False
    
    # if the last characters are the same, remove the last letters
    # and call the function with the new character sets (cs)
    if cs1[-1] == cs2[-1]:
        return is_subsequence(cs1[:-1], cs2[:-1])
    
    # if the last characters are not the same, keep removing the last
    # character of the superset-cs2 until the character is matched
    if cs1[-1] != cs2[-1]:
        return is_subsequence(cs1[:], cs2[:-1])

test_cases = [("xyz", "abxyzt"), ("xyz", "zabxyt")] 
res = [is_subsequence(cs1, cs2) for cs1, cs2 in test_cases]
res