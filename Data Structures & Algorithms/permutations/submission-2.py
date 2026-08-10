class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # cur = [], rem = [1,2,3]
        # cur = [1], rem = [2,3] -> cur = [1,2] , rem = [3] ++ cur = [1,3], rem = [2] -> cur = [1,2,3], rem = [] and cur = [1,3,2]
        # cur = [2], rem = [1,3]
        # cur = [3], rem = [1,2]


        def dfs(cur, rem):
            if rem == []:
                res.append(cur.copy())
                return
            for i in range(len(rem)):
                cur.append(rem[i])
                dfs(cur, rem[:i] + rem[i+1:])
                cur.pop()
        
        dfs([],nums)
        return res
            