"""
211. Design Add and Search Words Data Structure · https://leetcode.com/problems/design-add-and-search-words-data-structure/
2026-10-11 · clean · 30m · skeleton: trie
O(n) time / O(n) space — For Add, we are searching through n at worst case where n is size of trie, for search, worstcase all of trie serached
"""




class Trie():
    def __init__(self):
        self.nodes = {}
        self.end = False

        ## "a" : <TrieObj>

class WordDictionary:

    def __init__(self):
        self.words = Trie()


    def addWord(self, word: str) -> None:

        cur = self.words

        for char in word:

            if not cur.nodes.get(char):
                cur.nodes[char] = Trie()

            cur = cur.nodes[char]

        cur.end = True

    def search(self, word: str) -> bool:

        cur = self.words

        stack = [(cur,word)]

        while stack:
            cur, word = stack.pop()

            if word == "":
                if cur.end:
                    return True

            elif word[0] == '.':
                for x in cur.nodes.values():
                    stack.append((x, word[1:]))
            else:
                if cur.nodes.get(word[0]):
                    stack.append((cur.nodes[word[0]], word[1:]))

        return False




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)