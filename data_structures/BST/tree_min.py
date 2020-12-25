from tree_node import Node

def tree_min(ro: Node) -> Node:

	if not ro.l:
		return None

	while ro.l:
		ro = ro.l

	return ro