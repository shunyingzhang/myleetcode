class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minH = [d / s for d, s in zip(dist, speed)]
        heapq.heapify(minH)
        t = 0
        while minH:
            m = heapq.heappop(minH)
            if m > t:
                t += 1
            else:
                return t
        return t