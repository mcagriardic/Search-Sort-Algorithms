"""
From Cracking the Coding Interview
Imagine a wall clock
Given a time, calculate the angle between the hour and minute hands
"""

def calculate_minute_angle(minute):
    return (360 / 60) * minute

def calculate_hour_angle(hour, minute):
    return (360 / 12) * hour +  (minute / 60) * 30

def get_angle_between(hour, minute):
    minute_angle = calculate_minute_angle(minute)
    hour_angle = calculate_hour_angle(hour, minute)
    return abs(hour_angle - minute_angle)

get_angle_between(7, 42)

"""
>> 21.0
"""