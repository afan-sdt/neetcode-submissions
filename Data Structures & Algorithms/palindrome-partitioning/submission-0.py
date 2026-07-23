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
                    print("appending to solution:", currString, prospect)
                    prospect.append(currString)
                    res.append(prospect[:])
                    prospect.pop()
                return
            if isPalindrome(currString):
                print("curr string is a palindrome: ", currString, "i = ", i)
                print("before append", prospect)
                prospect.append(currString)
                print("before backtrack", prospect)
                backtrack(prospect, i+1, s[i])
                print("before pop", prospect)
                prospect.pop()
                print("after pop:", prospect)
            backtrack(prospect, i+1, currString + s[i])
        backtrack([], 1, s[0])
        return res