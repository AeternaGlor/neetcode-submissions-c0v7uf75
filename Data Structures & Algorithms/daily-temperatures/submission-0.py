class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            j = i + 1
            div = 0
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    div = j - i
                    break
                j += 1
            res.append(div)

        return res