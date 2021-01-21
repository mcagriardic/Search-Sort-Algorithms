class TrieNode:
    def __init__(self):
        self.children = 26 * [None]
        self.is_end = False