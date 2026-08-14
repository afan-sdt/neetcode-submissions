class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #keep a tmp variable and add to it
        # if it is a valid word in the dictionary, 
        # see if you can break the rest of the string 
        # if you can, return True
        #if you reach the end and there's still characters in the tmp string, return false

        words = set(wordDict)
        memo = {}

        def dfs(index):
            if index in memo:
                return memo[index]
            # print(f"recursed on index: {index}")
            if index == len(s):
                # print("reached end")
                memo[index] = True
                return True
            
            tmp = ""
            for i in range(index, len(s)):
                tmp += s[i]
                if tmp in words:
                    if dfs(i+1):
                        memo[index] = True
                        return True
            
            if tmp != "":
                memo[index] = False
                return False
            memo[index] = True
            return True
        
        return dfs(0)
        