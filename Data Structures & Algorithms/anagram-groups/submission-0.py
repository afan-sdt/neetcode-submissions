class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for w in s:
                arr[ord(w)-ord('a')]+=1
            myMap[tuple(arr)].append(s)
        return myMap.values()
            

        