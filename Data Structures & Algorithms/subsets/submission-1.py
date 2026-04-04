class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(l):
            if l > len(nums) - 1:
                res.append(subset.copy()) # O(len(subset)) => O(n)
                return
            # add curr node
            subset.append(nums[l])
            dfs(l + 1)
            # not add (remove) curr node
            subset.pop()
            dfs(l + 1)
        
        dfs(0)
        return res

            
