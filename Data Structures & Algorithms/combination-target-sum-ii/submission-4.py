class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # this is basically combination sum but each candidate is chosen once
        candidates.sort()

        res = []
        def dfs(i, cur, total):

            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target: #gone past
                return
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()
            i+=1
            while i < len(candidates) and candidates[i-1] == candidates[i]:
                i+=1
            dfs(i, cur, total)
        dfs(0, [], 0)
        return res