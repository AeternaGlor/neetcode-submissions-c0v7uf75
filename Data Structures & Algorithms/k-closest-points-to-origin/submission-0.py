class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # n x logk
        for p in points:
            dist = p[0]**2 + p[1]**2
            heapq.heappush_max(heap, (dist, p[0], p[1]))
            if len(heap) > k:
                heapq.heappop_max(heap)
        
        res = []
        for p in heap:
            dist, x, y = p
            res.append([x, y])
        return res