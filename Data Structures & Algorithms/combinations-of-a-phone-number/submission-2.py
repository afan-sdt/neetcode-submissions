class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = ""
        mapping = {
            '2':'abc',
            '3':'def',
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': 'tuv',
            '9':'wxyz'
        }
        #how do I map from number -> letter
        # ord() = ord((digit - 2) * 3 + i)
        if digits == "":
            return []

        def backtrack(rest: str):
            nonlocal curr
            if rest == "":
                if len(curr) == len(digits):
                    res.append(curr[:])
                return
            listofChars = mapping[rest[0]]
            for i in listofChars:
                character =  i
                curr += character
                backtrack(rest[1:])
                curr = curr[:-1]
            backtrack(rest[1:])
        backtrack(digits)
        return res