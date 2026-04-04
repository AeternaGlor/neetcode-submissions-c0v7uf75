class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 1
        l = 0
        curr_set = set()
        curr_set.add(s[l])
        for r in range(1, len(s)):
            if s[r] not in curr_set:
                curr_set.add(s[r])
            else:
                while s[l] != s[r]:
                    curr_set.remove(s[l])
                    l += 1
                curr_set.remove(s[l])
                l += 1
                curr_set.add(s[r])
            
            max_len = max(max_len, r - l + 1)
            # print(s[l:r+1])

        return max_len

            

