class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # represents letters in s1
        if len(s1) > len(s2):
            return False
        s1count = [0]*26
        for s in s1:
            s1count[ord(s)-ord('a')] +=1
        #represents letters in s2
        s2count = [0]*26
        for s in range(len(s1)):
            s2count[ord(s2[s]) - ord('a')] +=1
        matches = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches+=1
        l, r = 0, len(s1)
        while r < len(s2):

            print(l, r)
            #print(d1, d2)
            #check if hashmaps are equal
            if matches == 26:
                return True
            #advance r and l
            ind = ord(s2[l])-ord('a')
            s2count[ind] -= 1
            if s2count[ind] + 1 == s1count[ind]:
                matches -=1
            elif s2count[ind] == s1count[ind]:
                matches+=1
            #update d2 hashmap
            ind = ord(s2[r])-ord('a')
            s2count[ind] += 1
            if s2count[ind]-1 == s1count[ind]:
                matches-=1
            elif s2count[ind] == s1count[ind]:
                matches+=1
            l += 1
            r += 1
        return matches == 26
        