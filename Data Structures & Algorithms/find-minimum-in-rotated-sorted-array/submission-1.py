class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                # отсортирован
                res = min(res, nums[l])
                return res
            
            m = (r + l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # принадледит левой отсорт-ой части
                l = m + 1
            else:
                # принадледит правой отсорт-ой части
                r = m - 1
        return res
            