class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1         
        
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            res = res * 10 + digit
            if res > MAX or res < MIN:
                return 0
        return res
        
        
        
#         res = 0

#         MIN = -2147483648  # -2^31,
#         MAX = 2147483647  #  2^31 - 1 
        
#         while x:
#             digit = int(math.fmod(x, 10))
#             x = int(x / 10)
#             res = res * 10 + digit
#             if res > MAX or res < MIN:
#                 return 0
        
#         return res
        