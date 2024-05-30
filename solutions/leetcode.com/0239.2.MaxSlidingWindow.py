class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l, r = 0, 0
        result = []
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1
        return result
 
# metadata
# relevant-topics queue
# time-complexity O(N) 48.59%
# space-complexity O(N) 92.62%
# language python
# difficulty hard
# date 20240530