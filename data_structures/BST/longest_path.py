def bfs(ro):
    
    q=[ro]
    bfs = []

    while q:
        if q[0].l:
            q.append(q[0].l)
        if q[0].r:
            q.append(q[0].r)
        bfs.append(q.pop(0))
        
    return bfs


def visit_ro(ro, vts, path=[], intersection=[]):
    if not ro:
        return path,intersection 
    
    if path:
        if path[-1] == vts:
            return path, intersection

    if ro.l and ro.r:
        intersection.append(ro)
    
    path.append(ro.v)
    path, intersection = visit_ro(ro.l, vts, path=path[:], intersection=intersection)
    
    if not ro.l and not ro.r:
        if ro.v == vts:
            return path, intersection
        while path[-1] != intersection[-1].v:
            path.pop()
        intersection.pop()
        return path, intersection
    
    path, intersection = visit_ro(ro.r, vts, path=path[:], intersection=intersection)
    return path, intersection


def get_longest_path(ro):
    # find the node at the most outer layer for LEFT subtree
    el = bfs(ro.l)[-1].v
    # find the node at the most outer layer for RIGHT subtree
    er = bfs(ro.r)[-1].v
    # visit these nodes and return the path to them
    lpl = visit_ro(ro.l, el, path=[], intersection=[])[0]
    lpr = visit_ro(ro.r, er, path=[], intersection=[])[0]
    
    # combine the paths
    return lpl[::-1] + [ro.v] + lpr