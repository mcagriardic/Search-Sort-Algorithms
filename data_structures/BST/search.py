from tree_node import Node

def search(ro: Node, vts: int) -> Node:

    if not ro:
        return None

    if ro.v < vts:
        return search(ro.r, vts)
    elif ro.v > vts:
        return search(ro.l, vts)
    else:
        return ro