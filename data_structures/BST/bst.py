from tree_node import Node

class BST:
    def __init__(self, ro):
        self.ro = ro


    def __traverse(self, ro, order):
        if not ro:
            return None
        
        if order == "pre":   print(ro.v)
        self.__traverse(ro.l, order=order)
        if order == "in":    print(ro.v)
        self.__traverse(ro.r, order=order)
        if order == "post":  print(ro.v)

    def traverse(self, order="post"):
        self.__traverse(self.ro, order=order)


    def __search(self, ro, vts):

        if not ro:
            print("Binary search tree does not contain %s..." %vts)
            return None
        
        if vts < ro.v:
            self.__search(ro.l, vts)
        elif vts > ro.v:
            self.__search(ro.r, vts)
        else:
            print("Found it!...")
            
    def search(self, vts):
        self.__search(self.ro, vts)


    def __insert(self, ro, vti):
        
        if not ro:
            return Node(vti)

        if vti <= ro.v:
            ro.l = self.__insert(ro.l, vti)
        else:
            ro.r = self.__insert(ro.r, vti)

        return ro
                
    def insert(self, vti):
        if not isinstance(vti, list):
            vti = [vti]
        [self.__insert(self.ro, v) for v in vti]


    def __delete(self, ro, vtd):
        if not ro:
            return None
            
        if ro.v > vtd:
            ro.l = self.__delete(ro.l, vtd)
        elif ro.v < vtd:
            ro.r = self.__delete(ro.r, vtd)
        else: # ro.v == vtd
            if not ro.r:
                return ro.l
            elif not ro.l:
                return ro.r
            elif ro.l and ro.r:
                temp = ro.r
                while temp.l:
                    temp = temp.l
                
                ro.r = self.__delete(ro.r, temp.v)
                ro.v = temp.v

        return ro

    def delete(self, vtd):
        self.__delete(self.ro, vtd)
