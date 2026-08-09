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
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res