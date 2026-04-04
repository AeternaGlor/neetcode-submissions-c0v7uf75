class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        nums.sort()

        def helper(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # include
            subset.append(nums[i])
            helper(i + 1)
            
            # exclude all nums[j] == nums[i]
            subset.pop()
            while (i < len(nums) - 1 and 
                    nums[i] == nums[i + 1]):
                i += 1
            # указываем на элемент ПОСЛЕ дубликатов/выходим за границы
            helper(i + 1) 
        
        helper(0)
        return res



