class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for i in range(len(s)):
            count[s[i]] = i
        
        size = 0
        end = 0
        output = []
        
        for i in range(len(s)):
            size += 1
            end = max(end, count[s[i]])
            # if i == 0 and count[s[i]] == 0:
            #     output.append(size)
            #     size = 0
            #     continue 
            # if i != 0 and i == end:
            if i == end:
                # return [end, count[s[i]], size] 
                output.append(size)
                size = 0
                continue    
            
        if size:
            output.append(size)
        
        return output
       
            
            
        