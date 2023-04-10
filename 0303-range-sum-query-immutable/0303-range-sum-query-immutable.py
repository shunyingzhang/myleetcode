class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            l = self.prefix[left - 1]
        else:
            l = 0
        r = self.prefix[right] 
        
        return r - l
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)