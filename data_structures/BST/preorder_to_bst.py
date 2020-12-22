from tree_node import Node

def preorder_to_bst(l):
    if not l:
        return None
    
    ro = Node(l[0])
    ro.l = preorder_to_bst([e for e in l if e < l[0]])
    ro.r = preorder_to_bst([e for e in l if e > l[0]])
    
    return ro