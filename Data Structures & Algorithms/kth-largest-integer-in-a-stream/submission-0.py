class MinHeap:
    def __init__(self, nums):
        self.heap = self.heapify(nums)

    def heapify(self, heap):
        if len(heap) < 1: return [float("-inf")]

        # освобождаем ячейку с индексом 0
        heap.append(heap[0])
        heap[0] = float("-inf")

        cur = (len(heap) - 1) // 2
        # -1 т.к. до этого добавили 0 элемент в конец
        while cur > 0:
            # perlocate down from every node with children
            i = cur
            while 2  * i < len(heap):
                if (2 * i + 1 < len(heap) and
                    heap[2 * i + 1] < heap[2 * i] and
                    heap[2 * i + 1] < heap[i]):
                    # swap with right child (smallest)
                    heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                    i = 2 * i + 1 # проверим, может ли нода занимать это место или нужно спустить её ниже
                elif heap[2 *  i] < heap[i]:
                    # swap with left child (smallest)
                    heap[i], heap[2 * i] = heap[2 * i], heap[i]
                    i = 2 * i
                else:
                    # вершина стоит на своём месте (верху кучи/ нужной подкучи)
                    break
            cur -= 1
        return heap

    def pop(self):
        if len(self.heap) <= 1: 
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap):
            # perlocate down from new top
            if (2 * i + 1 < len(self.heap) and
                self.heap[2 * i + 1] < self.heap[2 * i] and
                self.heap[2 * i + 1] < self.heap[i]):
                # swap with right child
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                # swap with left child
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                # order correct
                break
        return res
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        # percolate up (through parents)
        while ( # иначе не работает с отрицательными
                self.heap[i] < self.heap[i // 2]):
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self. k = k
        self.heap = MinHeap(nums)
        while len(self.heap.heap) > k + 1:
            self.heap.pop()


    def add(self, val: int) -> int:
        heap = self.heap.heap
        # print(heap)

        if len(heap) < self.k + 1:
            self.heap.push(val)
        elif heap[1] < val:
            # print(11111)
            self.heap.pop()
            self.heap.push(val)

        # print(heap[1], val)
        return heap[1]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)