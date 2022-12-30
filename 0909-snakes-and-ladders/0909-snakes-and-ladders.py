class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n = len(board)
        
        def inttoindx(number):
            r = (number - 1) // n
            c = (number - 1) % n
            if r % 2 != 0:
                c = n - c -1
            return [r, c]
        
        q = deque()
        q.append([1, 0])
        visited = set()
        
        while q:
            num, step = q.popleft()
            for j in range(1, 7):
                nxt = num + j
                
                r, c = inttoindx(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                    
                if nxt == n * n:
                    return step + 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append([nxt, step + 1])
  
        return -1
        
        
#         brdlist = [-1] * length

#         for i in range(n - 1, -1, -1):
#             if (n - 1 - i) % 2 == 0:
#                 for j in range(n):
#                     if board[i][j] != -1:
#                         brdlist[(n - i - 1) * n + j] = board[i][j]
#             else:
#                 for j in range(n - 1, -1, -1):
#                     if board[i][j] != -1:
#                         brdlist[(n - i - 1) * n + (n - j - 1)] = board[i][j]  

#         # return brdlist       
#         q = collections.deque()
#         q.append(0)
#         step = 0
#         visited = set()
#         while q:
#             step += 1
#             for i in range(len(q)):
#                 num = q.popleft()
#                 visited.add(num)
#                 for j in range(1, 7):
#                     if num + j + 1 == length:
#                         return step
#                     if brdlist[num + j] != -1:
#                         if brdlist[num + j] == length:
#                             return step
#                         if brdlist[num + j] - 1 not in visited:
#                             q.append(brdlist[num + j] - 1)
#                     else:
#                         q.append(num + j)
        
#         return -1