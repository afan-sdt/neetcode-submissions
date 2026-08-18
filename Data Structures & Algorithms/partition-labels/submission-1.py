class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # construct a counts dict
        counts = {}
        for i in s:
            counts[i] = 1 + counts.get(i, 0)
        # have a curr letter counts which represents the letters in the current window
        curr = {}
        #when this curr dict is empty, we add the current length to res array
        currCount = 0
        res = []
        for ch in s:
            if ch in curr:
                curr[ch] -= 1
                if curr[ch] == 0:
                    curr.pop(ch)
            elif ch not in curr:
                curr[ch] = counts[ch] - 1
                if curr[ch] == 0:
                    curr.pop(ch)
                counts.pop(ch)
            currCount+=1
            if len(curr) == 0:
                res.append(currCount)
                currCount = 0
        return res
