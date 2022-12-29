class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        odmap = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) -1):
            w1 = words[i]
            w2 = words[i + 1]
            
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if odmap[w1[j]] > odmap[w2[j]]:
                    return False
                if odmap[w1[j]] < odmap[w2[j]]:
                    break
                
        return True
        