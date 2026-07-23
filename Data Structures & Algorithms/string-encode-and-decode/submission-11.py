class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += i
            res += '`'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        #iterate through the string
        # add each character to curr until we hit #
        # when we hit #, we add curr to the result list and reset curr
        curr = ""
        res = []
        for i in s:
            if i == '`':
                res.append(curr)
                curr = ""
            else:
                curr += i
        print(res)
        return res
