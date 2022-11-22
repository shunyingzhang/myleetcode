class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize :
            return False
        
        count = {}
        
        for h in hand:
            count[h] = 1 + count.get(h, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        
        while minH:
            g = minH[0]
            for j in range(groupSize):
                if g + j not in count:
                    return False
                if count[g + j] == 0:
                    return False
                count[g + j] -= 1
                if count[g + j] == 0:
                    heapq.heappop(minH)
        return True
            
        