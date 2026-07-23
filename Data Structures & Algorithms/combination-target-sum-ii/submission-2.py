class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # pick whether to add an element or not
        # keep track of current 
        #key idea: sort the input array, skip duplicates in 
        # the decision tree where one of those numbers was taken
        def dfs(i: int, path: List[int], total: int):
            if total == target:
                res.append(path.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            path.append(candidates[i])
            dfs(i+1, path, total + candidates[i])
            path.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, path, total)
        candidates.sort()
        dfs(0,[], 0)
        return res


        
        # res = set()
        # def dfs(i: int, path: List[int], total: int):
        #     if total == target:
        #         result = path.copy()
        #         result.sort()
        #         res.add(tuple(result))
        #         return
        #     if i >= len(candidates) or total > target:
        #         return
        #     #don't add it to the path
        #     # print(path)
        #     path.append(candidates[i])
        #     dfs(i+1, path, total + candidates[i])
        #     path.pop()
        #     dfs(i+1, path, total)
        # dfs(0, [], 0)
        # myList = list(res)
        
        # return [list(x) for x in myList]