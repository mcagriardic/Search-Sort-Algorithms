from search import search
from tree_min import tree_min
from tree_node import Node

def inorder_successor(ro: Node, v: int) -> Node:

	nv = search(ro, v)

	if nv.r:
		return nv.r
	else:
		y = nv.p
		while y:
			if y.v > nv.v:
				return y
			y = y.p

		return None