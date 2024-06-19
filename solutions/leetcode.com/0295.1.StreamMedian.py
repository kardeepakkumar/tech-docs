class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.insert(bisect.bisect_left(self.nums, num), num)

    def findMedian(self) -> float:
        if len(self.nums) % 2:
            return self.nums[len(self.nums)//2]
        else:
            return (self.nums[len(self.nums)//2 - 1] + self.nums[len(self.nums)//2])/2


# metadata
# relevant-topics binary search
# time-complexity O(NlogN) 12.39%
# space-complexity O(1) 93.12%
# language python
# difficulty hard
# date 20240601