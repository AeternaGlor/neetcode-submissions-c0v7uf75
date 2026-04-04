class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = {}
        for i in nums:
            cnt[i] = cnt.get(i, 0) + 1
        max_len = 0
        
        for k in cnt:
            j = k
            curr_len = 1
            # Добавил вот это
            if j - 1 in cnt:
                continue
            
            while True:
                if j + 1 in cnt:
                    curr_len += 1
                    j += 1
                else:
                    max_len = max(curr_len, max_len)
                    break
        return max_len