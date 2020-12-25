from tree_node import Node

def tree_max(ro: Node) -> Node:
    if not ro.r:
        return None

    while ro.r:
        ro = ro.r

    return ro