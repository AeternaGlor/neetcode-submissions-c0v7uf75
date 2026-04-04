class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        # candidates.sort()

        def helper(i, res, subset, accSum):
            print(subset)
            print(accSum)
            print(i)
            if (i >= len(candidates) or
                accSum > target):
                return
            
        
            if accSum == target: 
                res.append(subset.copy())
                return
            
            # include
            for i in range(i, len(candidates)):
                accSum += candidates[i]
                subset.append(candidates[i])
                helper(i, res, subset, accSum)
                
                accSum -= candidates[i]
                subset.pop()
            
            return
            # exclude
                
    
        
        helper(0, res, subset, 0)
        return res
