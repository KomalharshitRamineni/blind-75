 
"""
208. Implement Trie · https://leetcode.com/problems/implement-trie-prefix-tree/
2026-10-10 · clean · 25m · skeleton: trie
O(n) time / O(t) space — O(n) per function call and o(t) meaning the total number of trie nodes created.
"""


class Trie:

    def __init__(self):
        self.children = [None]*26
        self.end = False
        

    def insert(self, word: str) -> None:
        #Insert word into trie
        letter = 0

        cur = self

        while letter < len(word):

            key = ord(word[letter])-ord('a')

            if not cur.children[key]:
                cur.children[key] = Trie()

            cur = cur.children[key]
            letter += 1

        cur.end = True




    def search(self, word: str) -> bool:

        
        cur = self
        letter = 0

        while letter < len(word):

            key = ord(word[letter])-ord('a')

            if not cur.children[key]:
                return False

            cur = cur.children[key]
            letter += 1

        return True if cur.end else False

    def startsWith(self, prefix: str) -> bool:
        
        word = prefix
        cur = self
        letter = 0

        while letter < len(word):

            key = ord(word[letter])-ord('a')

            if not cur.children[key]:
                return False

            cur = cur.children[key]
            letter += 1

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)