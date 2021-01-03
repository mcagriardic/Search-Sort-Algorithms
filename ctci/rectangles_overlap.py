"""
From my interviewcake.com question of the week email:
Write an algorithm that determines if two rectangles overlap on an xy grid.
A rectangle is defined as a dictionary like the below:
rectangle_one = {
    'left_x' : 1,
    'bottom_y' : 1,
    'width' : 6,
    'length' : 3
}
rectangle_two = {
    'left_x' : 5,
    'bottom_y' : 2
    'width' : 3,
    'length' : 6
}
These overlap at the coordinates (x, y) [(6,3), (6,4), (7,3), (7,4)]
The return only needs to be True/False
Assume they are never diagonal and each side is parallel.
"""

def get_xy_low_high(r):
    xl = r["left_x"]
    yl = r["bottom_y"]
    xh = r["left_x"] + r["width"]
    yh = r["bottom_y"] + r["length"]
    return xl, yl, xh, yh

def is_overlap(r1, r2):
    xl1, yl1, xh1, yh1 = get_xy_low_high(r1)
    xl2, yl2, xh2, yh2 = get_xy_low_high(r2)

    for x in range(xl1, xh1 + 1):
        if x == xl2 or x == xh2:
            return True
    for y in range(yl1, yh1 + 1):
        if y == yl2 or y == yh2:
            return True
    return False

r1={
    'left_x' : 1,
    'bottom_y' : 1,
    'width' : 6,
    'length' : 3
}
r2={
    'left_x' : 5,
    'bottom_y' : 2,
    'width' : 3,
    'length' : 6
}

is_overlap(r1,r2)

"""
>> True
"""

r1={
    'left_x' : 1,
    'bottom_y' : 1,
    'width' : 1,
    'length' : 1
}
r2={
    'left_x' : 5,
    'bottom_y' : 3,
    'width' : 3,
    'length' : 6
}

is_overlap(r1,r2)

"""
>> False
"""