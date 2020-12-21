# retrieve the paths to leaves

def get_paths_to_leaves(ro, path=[]):
    if not ro:
        return [path]

    path.append(ro.v)
    paths = []
    # these if statements are the prevent finalising the execution
    # for nodes with missing one branch; left or right
    if (not ro.r) or (ro.l and ro.r) or (not ro.l and not ro.r):
        paths += [p for p in get_paths_to_leaves(ro.l, path=path[:]) if p not in paths]        
    if (not ro.l) or (ro.l and ro.r) or (not ro.l and not ro.r):
        paths += [p for p in get_paths_to_leaves(ro.r, path=path[:]) if p not in paths]
    return paths

