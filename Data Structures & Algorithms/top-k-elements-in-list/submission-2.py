class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first we should construct a frequency array that maps the frequency to the value
        # then we sort by frequency
        # then we take the highest
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        sorted_freq = list(sorted(freq.items(), key = lambda val: val[1]))
        vals = [x[0] for x in sorted_freq]
        print(vals)
        return vals[-k:]