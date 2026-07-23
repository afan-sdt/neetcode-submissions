class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(toCheck: str)-> bool:
            i, j = 0, len(toCheck)-1
            while i <= j:
                if toCheck[i] != toCheck[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def backtrack(prospect: List[List[str]], i: int, currString: str ):
            if i == len(s):
                print(currString)
                print(prospect)
                if isPalindrome(currString):
                    prospect.append(currString)
                    res.append(prospect[:])
                    prospect.pop()
                return
            if isPalindrome(currString):
                prospect.append(currString)
                backtrack(prospect, i+1, s[i])
                prospect.pop()
            backtrack(prospect, i+1, currString + s[i])
        backtrack([], 1, s[0])
        return res