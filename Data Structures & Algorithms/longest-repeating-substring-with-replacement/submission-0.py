class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        counts = [0] * 26
        res = 0
        windowLen = right - left + 1
        while right < len(s):
            counts[ord(s[right]) - ord('A')] += 1
            windowLen = right - left + 1
            if (windowLen - max(counts)) <= k:
                res = max(windowLen, res)
            else:
                while (windowLen - max(counts)) > k:
                    counts[ord(s[left])-ord('A')]-=1
                    left += 1
                    windowLen = right - left + 1
            right += 1
        return res
