class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = sorted(nums[0:k])
        result = [window[-1]]
        for i in range(0, len(nums)-k):
            del_idx = bisect.bisect_left(window, nums[i])
            window.pop(del_idx)
            ins_idx = bisect.bisect_left(window, nums[i+k])
            window.insert(ins_idx, nums[i+k])
            result.append(window[-1])
        return result
    
# metadata
# relevant-topics binary search, sliding window
# time-complexity O(NlogN) 5.00%
# space-complexity O(N) 40.34%%
# language python
# difficulty hard
# date 20240530