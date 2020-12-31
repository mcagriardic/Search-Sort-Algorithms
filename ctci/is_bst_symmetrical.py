class Node:
    
    def __init__(self, v, r=None, l=None):
        self.v = v
        self.r = r
        self.l = l

class BST:
    def __init__(self, ro):
        self.ro = ro

    # vti -> value to insert
    def __insert(self, ro, vti):
        if not ro:
            return Node(vti)

        if vti <= ro.v:
            ro.l = self.__insert(ro.l, vti)
        else:
            ro.r = self.__insert(ro.r, vti)

        return ro
                
    def insert(self, vti):
        if not isinstance(vti, list):
            vti = [vti]
        [self.__insert(self.ro, v) for v in vti]

def height(ro):
    if not ro:
        return 0
    
    return max(height(ro.l), height(ro.r)) + 1

def is_bst_symmetrical(ro):
    if not ro:
        return True
    
    lh = height(ro.l)
    rh = height(ro.r)

    if (
        abs(lh-rh) == 0
        and
        is_bst_symmetrical(ro.l)
        and
        is_bst_symmetrical(ro.r)
    ):
        return True
    
    return False

### EXAMPLE 1:
#       6
#    /     \
#   4       8
#  / \     / \
# 3   5   7   9

ro = Node(6)
bst = BST(ro)
bst.insert(
    [4,8,3,5,7,9]
)

is_bst_symmetrical(ro)

"""
>> True
"""


### EXAMPLE 2:
#       6
#    /     \
#   4       8
#  / \     /
# 3   5   7

ro = Node(6)
bst = BST(ro)
bst.insert(
    [4,8,3,5,7]
)

is_bst_symmetrical(ro)

"""
>> False
"""