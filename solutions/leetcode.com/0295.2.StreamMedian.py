class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1*num)
        
        if len(self.minHeap) > 1 + len(self.maxHeap):
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*num)
        if len(self.maxHeap) > 1 + len(self.minHeap):
            num = -1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return -1*self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0])/2

# metadata
# relevant-topics minHeap, maxHeap
# time-complexity O(N) 82.95%
# space-complexity O(1) 82.31%
# language python
# difficulty hard
# date 20240601