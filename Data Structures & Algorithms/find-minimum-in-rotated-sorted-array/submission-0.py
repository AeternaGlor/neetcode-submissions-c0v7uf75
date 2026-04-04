class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] < nums[r]: 
                # справа точно минимума не будет, 
                # так как последовательность возрастает
                r = m
            else:
                # возможно, только если начало последовательности 
                # (и минимум) правее медианы
                l = m
        return min(nums[l], nums[r])
            