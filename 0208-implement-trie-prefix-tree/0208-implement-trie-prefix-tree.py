class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.child[i] == None:
                cur.child[i] = TrieNode()
            cur = cur.child[i]
        cur.end = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.child[i] == None:
                return False
            cur = cur.child[i]
        return cur.end
            
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.child[i] == None:
                return False
            cur = cur.child[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)