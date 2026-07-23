class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        

        def backtrack(path: str, openCount: int, closeCount: int):
            if closeCount == 0:
                results.append(path)
                return
            
            if openCount > 0:
                path+='('
                backtrack(path, openCount-1, closeCount)
                path = path[:-1]
            if closeCount > openCount:
                path+=')'
                backtrack(path, openCount, closeCount-1)
                path = path[:-1]

        #actual function call
        backtrack("", n, n )
        return results

        