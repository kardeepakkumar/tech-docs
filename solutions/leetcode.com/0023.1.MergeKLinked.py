# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        currs = [head for head in lists]
        result = ListNode()
        resultCurr = result
        while True:
            element = float("infinity")
            for curr in currs:
                if curr and curr.val < element:
                    element = curr.val
            if element == float("infinity"):
                break
            for i in range(len(currs)):
                if currs[i] and currs[i].val == element:
                    resultCurr.next = currs[i]
                    resultCurr = resultCurr.next
                    currs[i] = currs[i].next
        result = result.next
        return result
    
# metadata
# relevant-topics linked lists
# time-complexity O(len(lists)*maxlength(list in lists) 21.16%
# space-complexity O(1) 72.47%
# language python
# difficulty hard
# date 20240601