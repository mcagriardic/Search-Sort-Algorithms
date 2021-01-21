from TrieNode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def char_to_index(self, c):
        return ord(c) - ord('a')

    def insert(self, cs):
        # ctn -> current trie node
        ctn = self.root
        cs = cs.lower()
        for i, c in enumerate(cs):
            c_ascii_idx = self.char_to_index(c)
            if not ctn.children[c_ascii_idx]:
                ctn.children[c_ascii_idx] = TrieNode()
            ctn = ctn.children[c_ascii_idx]
        ctn.is_end = True
        
    def __get_all_words(self, ro, word=[]):
        words = []
        if not ro.children:
            return [word]
        if ro.is_end:
            words.append(word)
        for i, c in enumerate(ro.children):
            if c:
                ew = self.__get_all_words(c, word=word + [chr(ord('a') + i)])
                for w in ew:
                    words.append(w)
        return words
    
    def get_all_words(self):
        for ws in self.__get_all_words(self.root):
            yield "".join(ws)
            
    def search(self, key):
        # ctn -> current trie node
        ctn = self.root
        for c in key:
            c_ascii_idx = self.char_to_index(c)
            if not ctn.children[c_ascii_idx]:
                return False
            ctn = ctn.children[c_ascii_idx]
        return True
    
    # delete implemetion on Trie with a tail recursion
    def __delete(self, key, ro, i):
    	# here the ro.children is essentially the list that holds the current
    	# letter (and others if any). if we are deleting "abc" and let's say
    	# that we are at letter c; essentially the children of letter c will
    	# be ro.children[<ascii_idx(c)>]
        c_ascii_idx = self.char_to_index(key[i])
        if key[i] == key[-1]:
        	# if the last letter has a children, then DO NOT delete the node
        	# change is_end to False and return the node as is
            if ro.children[c_ascii_idx]:
                ro.children[c_ascii_idx].is_end = False
                return ro
            # if however, the last letter hasn't got a children, return None
            # which will be carried over the call stack to previous call
            return None
        ro.children[c_ascii_idx] = self.__delete(key, ro.children[c_ascii_idx], i=i+1)
        return ro

    def delete(self, key):
        self.__delete(key, self.root, i=0)

t = Trie()
t.insert("abcd")
t.insert("abce")
t.insert("abc")
t.insert("abcef")
t.insert("abceg")
list(t.get_all_words())

"""
>> ['abc', 'abcd', 'abce', 'abcef', 'abceg']
"""

t.search("abc")

"""
>> True
"""

t.delete("abcef")
list(t.get_all_words())

"""
>> ['abc', 'abcd', 'abce', 'abceg']
"""

t.delete("abc")
list(t.get_all_words())

"""
>> ['abcd', 'abce', 'abceg']
"""