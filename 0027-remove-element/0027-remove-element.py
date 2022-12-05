class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        setVal = set()
        for i, n in enumerate(nums):
            if n == val:
                setVal.add(i)
                continue
            if setVal:
                nums[min(k, setVal.pop())] = n
            else:
                nums[k] = n
            k += 1 
                
        return k
        