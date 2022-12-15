class StockSpanner:

    def __init__(self):
        self.stack = []
        self.res = []
        

    def next(self, price: int) -> int:
        self.stack.append(price)
        i = len(self.stack) - 1
        span = 1
        while i - 1 >= 0 and self.stack[i - 1] <= price:
            span += self.res[i - 1]
            i -= self.res[i - 1]
        self.res.append(span)
        return span
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)