class TimeMap:

    def __init__(self):
        self.myMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(nums: List) -> str:
            res = ""
            l,r = 0, len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid][0] <= timestamp:
                    res = nums[mid][1]
                    l = mid+1
                else:
                    r = mid-1
            return res
        return binary_search(self.myMap[key])
