"""
Cracking the Coding Interview
Write a function which computes the number of trailing zeros in n factorial
"""

def findTrailingZeros(n): 
      
    # Initialize result 
    count = 0
  
    i = 5
    while n % 5 == 0 or n>5: 
      n = int(n/i)
      count += n
      
    return count

findTrailingZeros(50)

"""
>> 12
"""

findTrailingZeros(26)

"""
>> 6
"""

findTrailingZeros(6)

"""
>> 1
"""