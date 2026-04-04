class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = [(math.sqrt(p[0]**2 + p[1]**2), i) for i, p in enumerate(points)]

        heapq.heapify(distances)
        res = []
        for _ in range(k):
            idx = heapq.heappop(distances)[1]
            res.append(points[idx])
        return res