class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        setE = set()
        for e in emails:
            tmp1 = ''
            tmp2 = ''
            plus = 0
            for i, c in enumerate(e):
                if c == '+':
                    plus = 1
                    continue
                if c == '@':
                    e = e[i + 1:]
                    break
                if plus != 1 and c != '.':
                    tmp1 += c
            for c in e:
                tmp2 += c
            setE.add((tmp1, tmp2))
        
        return len(setE)
        