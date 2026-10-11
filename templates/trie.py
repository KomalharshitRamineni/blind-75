"""
trie — node with children dict + is_end flag

Trigger: prefix queries over a word set · matching many words against a grid or text simultaneously. Genuinely rare — 3 problems in Blind 75. Complexity: build O(total chars), query O(len)
"""






class TrieNode():
    def __init__(self):
        self.nodes = {}
        self.endOfWord = False


class Trie():
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word):

        #So we want to add this to our trie
        cur = self.node

        for char in word:

            #Check if key exists for char
            if not cur.nodes.get(char):
                cur.nodes[char] = TrieNode()
                
            cur = cur.nodes.get(char)

        cur.endOfWord = True

    def search(self, word):

        #So we want to add this to our trie
        cur = self.node

        for char in word:

            #Check if key exists for char
            if not cur.nodes.get(char):
                return False
                
            cur = cur.nodes.get(char)

        return cur.endOfWord


    def exists(self, word):

        #So we want to add this to our trie
        cur = self.node

        for char in word:

            #Check if key exists for char
            if not cur.nodes.get(char):
                return False
                
            cur = cur.nodes.get(char)

        return True
