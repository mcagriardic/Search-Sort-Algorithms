# Q4: Write a recursive function that checks whether a string
# is a palindrome (a palindrome is a string that's the same when
# reads forwards and backwards.)

def is_palindrome(cs):
    
    if len(cs) == 0 or len(cs) == 1:
        return True
              
    if not cs[0] == cs[-1]:
        return False
    
    return is_palindrome(cs[1:-1])

test_cases = ["adcba", "abxba", "abba"] 
res = [is_palindrome(tc) for tc in test_cases]
res