"""
from: Cracking the Coding Interview
Replace all spaces in a string with %20
"""

def replace_whitesape(cs):
    return cs.replace(" ", "%20")

replace_whitesape("Hello my name is John")

"""
>> 'Hello%20my%20name%20is%20John'
"""