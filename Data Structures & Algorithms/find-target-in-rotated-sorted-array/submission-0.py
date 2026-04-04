class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r  = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            
            if nums[m] > nums[r]:
                # слева от m послед-ть монотонно возрастает
                # (т.е) m относится к левой части
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # справа от m послед-ть монотонно возрастает
                # (т.е) m относится к правой части
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return - 1

