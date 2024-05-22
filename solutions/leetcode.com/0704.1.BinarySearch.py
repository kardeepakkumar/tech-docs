class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + ((end - start)//2) # Not using (start+end)//2 to mind overflow
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1


# metadata
# relevant-topics binary search
# time-complexity O(logN)
# space-complexity O(1)
# language python
# difficulty easy
# date 20240405