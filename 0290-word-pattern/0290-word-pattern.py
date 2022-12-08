class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = []
        ind = 0
        while ind < len(s):
            tmp = ''
            while ind < len(s) and s[ind] != ' ':
                tmp += s[ind]
                ind += 1
            ss.append(tmp)
            ind += 1
        # ss = s.split(' ')
        if len(ss) != len(pattern):
            return False

        mapPtoS = {}
        mapStoP = {}

        for i in range(len(pattern)):
            if pattern[i] in mapPtoS and mapPtoS[pattern[i]] != ss[i]:
                return False
            if ss[i] in mapStoP and mapStoP[ss[i]] != pattern[i]:
                return False
            mapPtoS[pattern[i]] = ss[i]
            mapStoP[ss[i]] = pattern[i]
        
        return True

       