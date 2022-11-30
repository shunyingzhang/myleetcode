class DetectSquares:

    def __init__(self):
        self.ptcount = defaultdict(int)
        self.pt = []
        

    def add(self, point: List[int]) -> None:
        self.ptcount[tuple(point)] += 1
        self.pt.append(point)
        

    def count(self, point: List[int]) -> int:
        px = point[0]
        py = point[1]
        res = 0
        
        for x, y in self.pt:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            
            res += self.ptcount[(x, py)] * self.ptcount[(px, y)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)