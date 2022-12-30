class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        q = deque()
        q.append(['0000', 0])
        visited = set(deadends)
        visited.add('0000')
        
        def findchildren(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[: i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[: i] + digit + lock[i + 1:])
            return res
        
        while q:
            lock, step = q.popleft()
            if lock == target:
                return step
            for child in findchildren(lock):
                if child not in visited:
                    visited.add(child)
                    q.append([child, step + 1])
        return -1
            
        