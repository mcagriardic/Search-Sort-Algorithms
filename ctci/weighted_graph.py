"""
Return all paths, ,plus their total "weight" in a graph
"""

g = G()

g.add_edge('1', '2', 1)
g.add_edge('2', '3', 6)
g.add_edge('2', '4', 2)
g.add_edge('4', '6', 2)
g.add_edge('3', '5', 1)
g.add_edge('6', '5', 1)

g.print_dict()

print g.find_all_paths('1', '5')