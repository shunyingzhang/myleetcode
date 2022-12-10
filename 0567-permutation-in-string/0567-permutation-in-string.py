class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1cnt = [0] * 26
        s2cnt = [0] * 26
        
        for i in range(len(s1)):
            s1cnt[ord(s1[i]) - ord('a')] += 1
            s2cnt[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(26):
            if s1cnt[i] == s2cnt[i]:
                match += 1
        
        if match == 26:
            return True
        
        for i in range(len(s1), len(s2)):
            
            indx = ord(s2[i]) - ord('a')
            s2cnt[indx] += 1
            if s1cnt[indx] == s2cnt[indx]:
                match += 1
            if s1cnt[indx] == s2cnt[indx] - 1:
                match -= 1
            
            indx = ord(s2[i - len(s1)]) - ord('a')
            s2cnt[indx] -= 1
            if s1cnt[indx] == s2cnt[indx]:
                match += 1
            if s1cnt[indx] == s2cnt[indx] + 1:
                match -= 1
            
            if match == 26:
                return True
        return False
            
        
        
        
#         if len(s1) > len(s2):
#             return False
        
#         s1count = [0] * 26
#         s2count = [0] * 26
        
#         for i in range(len(s1)):
#             s1count[ord(s1[i]) - ord('a')] += 1
#             s2count[ord(s2[i]) - ord('a')] += 1
            
#         matches = 0
#         for i in range(26):
#             if s1count[i] == s2count[i]:
#                 matches += 1 
                
#         if matches == 26:
#                 return True             
        
#         l = 0
#         for r in range(len(s1), len(s2)):
            
#             index = ord(s2[r]) - ord('a')
#             s2count[index] += 1
#             if s1count[index] == s2count[index]:
#                 matches += 1
#             elif s1count[index] + 1 == s2count[index]:
#                 matches -= 1
                
#             index = ord(s2[l]) - ord('a')
#             s2count[index] -= 1
#             if s1count[index] == s2count[index]:
#                 matches += 1
#             elif s1count[index] - 1 == s2count[index]:
#                 matches -= 1
                
#             if matches == 26:
#                 return True
#             l += 1
            
#         return False
