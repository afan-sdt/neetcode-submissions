class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = "".join(char for char in s if char.isalnum()).lower()
        print(cleanS)
        
        for i in range((len(cleanS)//2)):
            j = 0+i
            k = len(cleanS)-1-i
            if(cleanS[j]!=cleanS[k]):
                return False
        return True


        