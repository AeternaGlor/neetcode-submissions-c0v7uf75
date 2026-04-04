class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def recF(l):
            
            if l > len(nums) - 1:
                return
            recF(l+1)
            tmp = []
            for arr in res: # O(n)
                tmp.append(arr.copy()) # O(m = n) !!!!!!! ТУТ!!!!
                arr.append(nums[l])
            res.extend(tmp) # O(n)
            # print(l, res)
        recF(0)
        return res

        