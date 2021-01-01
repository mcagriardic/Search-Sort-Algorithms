"""
Cracking the Coding Interview
Write methods for the following operations:
subtraction,
multiply,
divide
and only use the add operation (+)
"""

def substract(n1, n2):
    minn = min(n1,n2)
    maxn = max(n1,n2)
    
    res = 0
    while minn != maxn:
        minn += 1
        res += 1
        
    return res

def multiply(n1, n2):
    res = 0
    for i in range (n2):
        res += n1
        
    return res

def divide(dividend, divisor, res="", dec=5):
    if "." in res:
        if len(res.split(".")[-1]) == dec:
            return res
    # tn -> temporary number            
    tn = 0
    quotient = 0
    while tn + divisor <= dividend:
        quotient += 1
        tn += divisor

    res += str(quotient)
    if tn == dividend:
        return res
    if "." not in res:
        res += "."
    
    if dividend > quotient:
        res = divide(
            multiply(
                10,
                # remainder
                substract(dividend, tn)
            ),
            divisor,
            res=res,
            dec=dec
        )
    return res

print(substract(15, 3) == 12)
print(multiply(8, 3) == 24)
print(divide(15, 7, dec=3) == '2.142')
print(divide(15, 7) == '2.14285')
print(divide(15, 3) == '5')

"""
>> True
>> True
>> True
>> True
>> True
"""
