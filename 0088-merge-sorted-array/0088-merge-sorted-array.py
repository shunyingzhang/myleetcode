class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n -1
        
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[p] = nums1[m - 1]
                m -= 1
                p -= 1
            elif nums1[m - 1] < nums2[n - 1]:
                nums1[p] = nums2[n - 1]
                n -= 1
                p -= 1
            else:
                nums1[p] = nums1[m - 1]
                nums1[p - 1] = nums1[m - 1]
                p -= 2
                m -= 1
                n -= 1
        if n > 0:
            for i in range(0, n):
                nums1[i] = nums2[i]
                
            
        
        