class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # each step we have the choice to add close or open paranthesis
        # if the number of close ever exceed number of open, we return
        res = []

        def dfs(curr, op, clo):
            if clo > n or op > n:
                return
            if clo > op:
                return
            if op == clo == n:
                print(curr)
                res.append("".join(curr))
                return
            
            # add open
            curr.append('(')
            dfs(curr, op+1, clo)
            curr.pop()
            curr.append(')')
            dfs(curr, op, clo + 1)
            curr.pop()
        dfs([],0, 0)
        return res