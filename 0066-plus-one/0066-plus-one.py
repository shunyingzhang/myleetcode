class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = digits[len(digits) -1]
        
        if d >= 0 and d < 9:
            digits[len(digits) -1] = d + 1
        else:
            digits[len(digits) -1] = 0
            if len(digits) == 1:
                return [1, 0]
            for i in range(len(digits) - 2, -1, -1):
                if digits[i] >= 0 and digits[i] < 9:
                    digits[i] += 1
                    return digits
                else:
                    if i > 0:
                        digits[i] = 0
                    else:
                        digits.append(0)
                        digits[0] = 1
                        
        
        return digits
                            
                            
                        
                
            