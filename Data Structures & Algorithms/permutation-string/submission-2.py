class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # represents letters in s1
        if len(s1) > len(s2):
            return False
        d1 = [0]*26
        for s in s1:
            d1[ord(s)-ord('a')] +=1
        #represents letters in s2
        d2 = [0]*26
        for s in range(len(s1)):
            d2[ord(s2[s]) - ord('a')] +=1
        l, r = 0, len(s1)
        while r < len(s2):

            print(l, r)
            print(d1, d2)
            #check if hashmaps are equal
            if d1 == d2:
                return True
            #advance r and l
            d2[ord(s2[l])-ord('a')] -= 1
            #update d2 hashmap
            d2[ord(s2[r])-ord('a')] += 1
            l += 1
            r += 1
        return d1==d2
        