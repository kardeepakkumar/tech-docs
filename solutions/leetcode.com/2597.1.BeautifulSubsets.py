class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        marked = set()
        nums.sort()
        batches = []
        counts = collections.Counter(nums)
        for i in range(0, len(nums)):
            n = nums[i]
            if n not in marked:
                marked.add(n)
                batches += [[n]]
                n += k
                while n <= nums[-1]:
                    if n in nums:
                        marked.add(n)
                        batches[-1] += [n]
                    else:
                        break
                    n += k                        
        def countBatches(batch):
            if len(batch) == 1:
                return 2**counts[batch[0]]
            elif len(batch) == 2:
                return (2**counts[batch[0]] + 2**counts[batch[1]] - 1)
            else:
                return (((2**counts[batch[0]])-1)*countBatches(batch[2:]) + countBatches(batch[1:]))
        result = 1
        for batch in batches:
            result *= countBatches(batch)
        result -= 1
        return result
    
# metadata
# relevant-topics recursion
# time-complexity O(N*LOG(N)) 90.73%
# space-complexity O(N) 15.18%
# language python
# difficulty medium
# date 20240523