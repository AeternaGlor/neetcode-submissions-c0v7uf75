class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list(map(lambda x: -x, stones))
        heapq.heapify(heap)
        res = 0
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(heap, stone1 - stone2)

        return -heap[0] if len(heap) > 0 else 0

