class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #add the sorted version of the string into a hash map, adding as you go along
        lists = defaultdict(list)
        for i in strs:
            tt = "".join(sorted(i))
            lists[tt].append(i)
        return [x for x in lists.values()]