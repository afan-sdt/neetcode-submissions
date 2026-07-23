class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0]*26
        countt = [0]*26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            countt[ord(t[i]) - ord('a')] += 1
        for i in range(26):
            if counts[i] != countt[i]:
                return False
        return True