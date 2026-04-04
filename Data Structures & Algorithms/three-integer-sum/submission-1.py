class Solution:
    def bucket_sort(self, nums):
        buckets = [0 for i in range(-10**5, 10**5)]
        res = []
        for n in nums:
            buckets[n] += 1
        for b in range(-10**5, 10**5):
            for i in range(buckets[b]):
                res.append(b)
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.bucket_sort(nums)
        print('nums')
        print(nums)
        print('nums')
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            l = i+1
            r = len(nums) - 1
            while l < r:
                print([nums[l], nums[r], -target])
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.add((nums[l], nums[r], -target))
                    r -= 1
                    l += 1


        return list(res)

        