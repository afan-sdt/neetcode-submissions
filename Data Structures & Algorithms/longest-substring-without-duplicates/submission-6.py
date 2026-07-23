class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l, r = 0, 0
        seen = {} # stores letters to index seen at
        while r < len(s):
            #if this letter has been seen, move left to 1 + lastseen index
            if s[r] in seen:
                temp = seen[s[r]] + 1
                while l < temp:
                    seen.pop(s[l])
                    l+=1
            maxLength = max(maxLength, r - l + 1)
            seen[s[r]] = r
            r+=1
        return maxLength