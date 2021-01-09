"""
Cracking the Coding Interview
Given two straight lines write a function which determines when they meet.
The lines are represented on a x, y grid. y and x is provided for each line.
Example:
    4|_|X|_|_|
    3|O|O|O|O|
    2|_|X|_|_|
    1|_|X|_|_|
     1 2 3  4
X = x_axis = (start: 2, end: 2)
    y_axis = (start: 1, end: 4)
    data_s = [[2,2], [1, 4]]
O = x_axis = (start: 1, end: 4)
    y_axis = (start: 3, end: 3)
    data_s = [[1,4], [3, 3]]
"""

import numpy as np

#l -> line
def standardise_coordinates(l):
    return np.subtract(l, 1).tolist()

def get_grid_edge(merged_coordinates):
    return max(max(merged_coordinates)) + 1

def create_line_coordinates_util(axis_s, axis_e, grid_edge):
    if axis_s == axis_e:
        return [axis_s] * grid_edge
    return [c for c in range(axis_s, axis_e + 1)]

def create_line_coordinates(l, grid_edge):
    coordinates = []
    xs, xe = l[0]
    ys, ye = l[1]
    x = create_line_coordinates_util(xs, xe, grid_edge)
    
    y = create_line_coordinates_util(ys, ye, grid_edge)
    return list(zip(x, y))

def has_common_coordinate(l1, l2):
    for c1 in l1:
        for c2 in l2:
            if c1 == c2:
                return np.add(c1, 1).tolist()
    return -1

def are_lines_overlap(l1, l2):
    l1,l2 = [standardise_coordinates(l) for l in [l1, l2]]
    grid_edge = get_grid_edge(l1 + l2)
    l1 = create_line_coordinates(l1, grid_edge)
    l2 = create_line_coordinates(l2, grid_edge)
    return has_common_coordinate(l1, l2)

## Complexity n^2 where n is the grid edge
are_lines_overlap([[2, 2], [1, 4]], [[1, 4], [3, 3]])

"""
>> (1, 2)
"""

def are_lines_overlap_alt(l1, l2):
    x1, y1 = l1
    x2, y2 = l2
    
    x1s, x1e = l1[0]
    y1s, y1e = l1[1]

    x2s, x2e = l2[0]
    y2s, y2e = l2[1]
    
    return list(zip(
        set(range(x1s, x1e + 1)) & set(range(x2s, x2e + 1)),
        set(range(y1s, y1e + 1)) & set(range(y2s, y2e + 1))
    ))

# Complexity n where n is the length of the longest line
are_lines_overlap_alt([[2, 2], [1, 4]], [[1, 4], [3, 3]])

"""
>> [(2, 3)]
"""

are_lines_overlap_alt([[1, 4], [1, 4]], [[1, 4], [1, 4]])

"""
>> [(1, 1), (2, 2), (3, 3), (4, 4)]
"""

are_lines_overlap_alt([[9, 13], [10, 10]], [[1, 4], [1, 4]])

"""
>> []
"""