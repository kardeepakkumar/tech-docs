class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        result = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, H = stack.pop()
                result = max(result, H*(i-idx))
                start = idx
            stack.append((start, h))
        return result
        
# metadata
# relevant-topics stack
# time-complexity O(N) 73.92%
# space-complexity O(N) 8.00%
# language python
# difficulty hard
# date 20240401
