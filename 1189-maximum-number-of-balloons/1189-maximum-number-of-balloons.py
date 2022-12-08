class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for c in text:
            if c in hmap:
                hmap[c] += 1
        hmap['l'] = hmap['l'] // 2
        hmap['o'] = hmap['o'] // 2 

        return min(hmap.values())   