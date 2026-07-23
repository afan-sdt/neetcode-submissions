class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def dfs(i: int, path: List[int], total: int):
            if total == target:
                result = path.copy()
                result.sort()
                res.add(tuple(result))
                return
            if i >= len(candidates) or total > target:
                return
            #don't add it to the path
            # print(path)
            path.append(candidates[i])
            dfs(i+1, path, total + candidates[i])
            path.pop()
            dfs(i+1, path, total)
        dfs(0, [], 0)
        myList = list(res)
        
        return [list(x) for x in myList]