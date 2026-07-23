class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res+= str(len(s))+ '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i=0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            print(s[i:j])
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j+length+1
        return res



