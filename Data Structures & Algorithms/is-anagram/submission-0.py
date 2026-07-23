class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0]*26
        for n in s:
            arr1[ord(n)-ord('a')]+=1
        for n in t:
            if arr1[ord(n)-ord('a')] == 0:
                return False
            arr1[ord(n)-ord('a')]-=1
        for n in arr1:
            if n != 0:
                return False
        return True
        