class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        l = 0
        r = len(people) - 1
        while l <= r:
            if people[r] == limit or people[l] + people[r] > limit:
                res += 1
                r -= 1
            else:
                res += 1
                r -= 1
                l += 1

        return res
                    
                    
        