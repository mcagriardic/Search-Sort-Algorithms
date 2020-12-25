from search import search
from tree_max import tree_max
from tree_node import Node

def inorder_predecessor(ro: Node, v: int) -> Node:
    # nv -> node value
    nv = search(ro, v)

    if nv.l:
        return tree_max(nv.l)
    else:
        y = nv.p
        while y:
            if y.v < nv.v:
                return y
            y = y.p

        return None