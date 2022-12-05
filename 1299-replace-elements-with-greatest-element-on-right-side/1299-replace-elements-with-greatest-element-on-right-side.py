class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        
        for i in range(len(arr) - 1, -1, -1):
            getMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = getMax
        
        return arr
        