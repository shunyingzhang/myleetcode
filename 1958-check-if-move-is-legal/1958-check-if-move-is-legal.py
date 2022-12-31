class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        
        def legal(rm, cm, color, d):
            length = 1
            while (0 <= rm < 8 and 0 <= cm < 8):
                length += 1
                if board[rm][cm] == '.':
                    return False
                if board[rm][cm] == color:
                    return  length >= 3
                rm += d[0]
                cm += d[1]
            return False
        
        
        for d in directions:
            if legal(rMove + d[0], cMove + d[1], color, d):
                return True
        
        return False
        
        
        