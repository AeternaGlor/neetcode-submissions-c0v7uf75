class MedianFinder:

    def __init__(self):
        self.large_minHeap = []
        self.small_maxHeap = []
        

    def addNum(self, num: int) -> None:
        if len(self.small_maxHeap) > len(self.large_minHeap):
            max_min = heapq.heappushpop_max(self.small_maxHeap, num)
            heapq.heappush(self.large_minHeap, max_min)
        else:
            min_max = heapq.heappushpop(self.large_minHeap, num)
            heapq.heappush_max(self.small_maxHeap, min_max)


    def findMedian(self) -> float:
        if len(self.small_maxHeap) == len(self.large_minHeap):
            return (self.large_minHeap[0] + self.small_maxHeap[0]) / 2
        else:
            return self.small_maxHeap[0]