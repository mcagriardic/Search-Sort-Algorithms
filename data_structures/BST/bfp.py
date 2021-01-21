"""Breadth first print ergo layerwise printing""" 

from collections import defaultdict


def bfp(ro):
    # Breadth first print ergo layerwise printing
    # node by layer
    nbl = defaultdict(lambda: [])
    q = [[ro]]
    
    # al -> at layer
    al = 1
    # ll -> last layer
    ll = 0

    # clc -> current layer node count 
    clc = 1
    # nlc -> next layer node count
    nlc = 0

    while q:
        # detect the layer change to layer header
        if ll != al:
            print(("\n" if al != 1 else "") + "Layer %s..." %al)
        
        # current node info in the form of tuple
        # cni -> (cn, pn, rtp)
        # cni -> current node information
        # cn -> current node
        # pn -> parent node
        # rtp -> relation to parent
        cni = q[0]
        if al == 1:
            print(cni[0].v)
            nbl[al] = [(cni[0].v,)]
        else:
            ttp = (
                "{0} * "      # Node value
                "{1} * "      # Relation to parent
                "{2}"         # Parent node value
            ).format(
                cni[0].v,
                cni[2],
                cni[1].v
                
            )
            print(ttp)
            nbl[al] = nbl[al] + [(cni[0].v, cni[1].v)]
        
        # last layer becomes the active layer
        ll = al
        clc -= 1

        q.pop(0)

        if cni[0].l:
            q.append((cni[0].l, cni[0], "l"))
            nlc += 1

        if cni[0].r:
            q.append((cni[0].r, cni[0], "r"))
            nlc += 1

        # when the nodes in the current layer are
        # finished
        if clc == 0:
            # change the clc to be next layer
            clc = nlc
            # restart the next layer
            nlc = 0
            # advance to next layer
            al += 1

    return nbl


# Alternative
from collections import defaultdict


def bfp(ro):
    queue = [ro]
    cl = 1
    nl = 0
    lc = 1
    layers = defaultdict(lambda: [])
    while queue:
        cl -= 1
        if queue[0].left:
            nl += 1
            queue.append(queue[0].left)
        if queue[0].right:
            nl += 1
            queue.append(queue[0].right)
        layers[lc].append(str(queue.pop(0).val))

        if cl == 0:
            lc += 1
            cl, nl = nl, 0

    for k in layers.copy():
        print("Layer %s ..." %k)
        print(" ".join(layers[k]))
        print("\n")