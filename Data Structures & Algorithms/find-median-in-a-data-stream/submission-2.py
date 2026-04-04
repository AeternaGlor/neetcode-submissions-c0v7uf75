class MinHeap:
    def __init__(self, nums=list()):
        self.heap = self.heapify(nums)
    
    def heapify(self, nums):
        if len(nums) < 1:
            return [0]
        
        nums.append(nums[0])

        cur = (len(nums) - 1) // 2
        while cur > 0:
            i = cur
            while 2 * i <= len(nums) - 1:
                if (2 * i + 1 <= len(nums) - 1 and
                        nums[2 * i + 1] < nums[2 * i] and
                        nums[2 * i + 1] < nums[i]):
                    nums[2 * i + 1], nums[i] = nums[i], nums[2 * i + 1]
                    i = 2 * i + 1
                elif nums[2 * i] < nums[i]:
                    nums[2 * i], nums[i] = nums[i], nums[2 * i]
                    i = 2 * i
                else:
                    break
            cur -= 1
        return nums
    
    def pop(self):
        if len(self.heap) <= 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i <= len(self.heap) - 1:
            if (2 * i + 1 <= len(self.heap) - 1 and
                    self.heap[2*i+1] < self.heap[2*i] and
                    self.heap[2*i+1] < self.heap[i]):
                self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                self.heap[2*i], self.heap[i] = self.heap[i], self.heap[2*i]
                i = 2 * i
            else:
                break
        return res
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while (i // 2 > 0 and
            self.heap[i] < self.heap[i // 2]):
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2


class MaxHeap:
    def __init__(self, nums=list()):
        self.heap = self.heapufy(nums)
    
    def heapufy(self, nums):
        if len(nums) < 1:
            return [0]
        
        nums.append(nums[0])

        cur = (len(nums) - 1) // 2
        while cur > 0:
            i = cur
            while 2 * i <= len(nums) - 1:
                if (2 * i + 1 <= len(nums) - 1 and 
                        nums[2 * i + 1] > nums[2 * i] and
                        nums[2 * i + 1] > nums[i]):
                    nums[i], nums[2 * i + 1] = nums[2 * i + 1], nums[i]
                    i = 2 * i + 1
                elif nums[2 * i] > nums[i]:
                    nums[i], nums[2 * i] = nums[2 * i], nums[i]
                    i = 2 * i
                else:
                    break
            cur -= 1
        return nums
    
    def pop(self):
        if len(self.heap) <=1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i <= len(self.heap) - 1:
            if (2*i+1 <= len(self.heap) - 1 and
                    self.heap[2*i+1] > self.heap[2*i] and
                    self.heap[2*i+1] > self.heap[i]):
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[2*i] > self.heap[i]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2 * i
            else:
                break
        
        return res
    
    def push(self, val):
        self.heap.append(val)

        i = len(self.heap) - 1
        while (i // 2 > 0 and
                self.heap[i // 2] < self.heap[i]):
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2



class MedianFinder:

    def __init__(self):
        self.large_minHeap = MinHeap()
        self.small_maxHeap = MaxHeap()
        

    def addNum(self, num: int) -> None:
        if len(self.small_maxHeap.heap) > len(self.large_minHeap.heap):
            self.small_maxHeap.push(num)
            max_min = self.small_maxHeap.pop()
            self.large_minHeap.push(max_min)
        else:
            self.large_minHeap.push(num)
            min_max = self.large_minHeap.pop()
            self.small_maxHeap.push(min_max)


    def findMedian(self) -> float:
        if len(self.small_maxHeap.heap) == len(self.large_minHeap.heap):
            return (self.large_minHeap.heap[1] + self.small_maxHeap.heap[1]) / 2
        else:
            return self.small_maxHeap.heap[1]

