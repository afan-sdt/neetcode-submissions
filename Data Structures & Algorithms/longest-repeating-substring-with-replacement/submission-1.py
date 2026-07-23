class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        counts = [0] * 26
        res = 0
        windowLen = right - left + 1
        maxF = 0
        while right < len(s):
            counts[ord(s[right]) - ord('A')] += 1
            maxF = max(maxF, counts[ord(s[right]) - ord('A')])
            windowLen = right - left + 1
            if (windowLen - maxF) <= k:
                res = max(windowLen, res)
            else:
                while (windowLen - maxF) > k:
                    counts[ord(s[left])-ord('A')]-=1
                    left += 1
                    windowLen = right - left + 1
            right += 1
        return res
