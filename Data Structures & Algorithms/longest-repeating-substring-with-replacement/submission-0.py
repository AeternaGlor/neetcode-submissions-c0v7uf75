class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        cnt = {}
        maxf = 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxf = max(maxf, cnt[s[r]])
            # можем эту переменную не уменьшать, так как 
            # нам важен лишь случай, конда её значение увеличилось...
            if (r - l + 1) - maxf > k:
                cnt[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len

