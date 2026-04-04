class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                val, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temperatures[i], i))
        
        while stack:
            val, idx = stack.pop()
            res[idx] = 0

        return res