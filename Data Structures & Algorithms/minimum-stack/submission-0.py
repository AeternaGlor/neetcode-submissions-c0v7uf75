class MinStack:

    def __init__(self):
        self.min_idxs = []
        self.lst = []
        
    def push(self, val: int) -> None:
        self.lst.append(val)
        # min_idx = self.min_idxs[-1]
        if not self.min_idxs or self.lst[self.min_idxs[-1]] > val:
            self.min_idxs.append(len(self.lst) - 1)
        
    def pop(self) -> None:
        if self.min_idxs[-1] == len(self.lst) - 1:
            self.min_idxs.pop()
        self.lst.pop()
        
    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        min_idx = self.min_idxs[-1]
        return self.lst[min_idx]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()