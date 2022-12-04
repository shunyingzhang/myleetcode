class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        for n in s:
            hashmap[n] = 1 + hashmap.get(n, 0)

        for n in t:
            if n not in hashmap:
                return False
            if hashmap[n] == 0:
                return False
            hashmap[n] -= 1
        
        return hashmap
            
        