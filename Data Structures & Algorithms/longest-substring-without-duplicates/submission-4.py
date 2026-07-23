class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #need two pointers to represent current window
        left, right = 0, 0

        #hashmap stores the letters in the current window
        #mapped to their indices
        mp = {}

        #res is the current max seen so far, start with 0
        res = 0

        #iterate through until right reaches the end
        while right < len(s):
            if s[right] in mp:
                #update left while removing from map
                temp = mp[s[right]] + 1
                while left < temp:
                    mp.pop(s[left])
                    left+=1
            mp[s[right]] = right
            res = max(res, right-left + 1)
            right+=1
        return res
