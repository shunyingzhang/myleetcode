class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        setE = set()
        for e in emails:
            tmp1 = ''
            i = 0
            while e[i] not in ['@', '+']:
                if e[i] != '.':
                    tmp1 += e[i]
                i += 1
            while e[i] != '@':
                i += 1
            tmp2 = e[i + 1:]
            
            setE.add((tmp1, tmp2))
        
        return len(setE)
        