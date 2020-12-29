"""
FROM CTCI:

Pond Size: You have an integer matrix representing a plot of land, where the value at that location
represents the height above sea level. A value of zero indicates water. A pond is a region of
water connected vertically or horizontally. The size of the pond is the total number of connected
water cells. Write a method to compute all possible ponds.

Note: CTCI is also looking for diagonal connections. It also asks developer to return the length of
the ponds.
"""

def filter_negative_index(e):
    # if any coordinate has a negative index
    if any(c < 0 for c in e):
        return 0
    return 1

# vertical index set upper limit
def vi_set_upper(e):
    if not e[0] < len(g):
        return 0
    return 1

# horizontal index set upper limit
def hi_set_upper(e):
    if not e[1] < len(g[0]):
        return 0
    return 1

def compute_neighbours(i, j):
    # vertical neighbour
    vn = [
        (i + 1, j),
        (i - 1, j)   
    ]
    
    # horizontal neighbour
    hn = [
        (i, j + 1),
        (i, j - 1)
    ]
    
    vn = filter(filter_negative_index, vn)
    vn = filter(vi_set_upper, vn)
    hn = filter(filter_negative_index, hn)
    hn = filter(hi_set_upper, hn)
    
    return list(vn) + list(hn)

def filter_zero_coordinate(e):
    # e -> (2, 3) coordinates
    if g[e[0]][e[1]] == 0:
        return 1
    return 0

# remove previous zero coordinate
def remove_processed_zc(nze, processed):
    return [nz for nz in nze if nz not in processed]

# get_neighbouring zero coordinates
def get_neighbouring_zc(r, c):
    n = compute_neighbours(r, c)
    return list(filter(filter_zero_coordinate, n))

def find_ponds(g):

    processed = set()
    ponds = []
    cc = len(g)
    rc = len(g[0])

    for r in range(rc):
        for c in range(cc):
            if g[r][c] == 0 and (r,c) not in processed:
                pond = set()
                pond.add((r,c))
                processed.add((r,c))
                # nzs -> non zero stack
                nzs = get_neighbouring_zc(r, c)
                while nzs:
                    last_nz = nzs.pop()
                    # non zero extended
                    nze = get_neighbouring_zc(last_nz[0], last_nz[1])
                    nzs = nzs + remove_processed_zc(nze, processed)
                    pond.add(last_nz)
                    processed.add(last_nz)
                if pond not in ponds:
                    ponds.append(pond)
    
    for pond in ponds:
        print("*** --- ***")
        print(pond)

g = [
    [0,2,1,0],
    [0,1,0,1],
    [0,0,0,1],
    [0,1,0,1],
]

# returns the coordinate of vertically or horizontally connected
# 0 elements
find_ponds(g)


"""
>>> *** --- ***
>>> {(1, 2), (3, 2), (0, 0), (3, 0), (2, 1), (2, 0), (2, 2), (1, 0)}
>>> *** --- ***
>>> {(0, 3)}
"""