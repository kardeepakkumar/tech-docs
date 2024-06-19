# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float("-infinity")
        self.maxGain(root)
        return self.result

    def maxGain(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        leftGain = max(self.maxGain(node.left), 0)
        rightGain = max(self.maxGain(node.right), 0)

        currentVal = node.val + leftGain + rightGain
        self.result = max(self.result, currentVal)

        return node.val + max(leftGain, rightGain)
    
# metadata
# relevant-topics binary tree, recursion
# time-complexity O(N) 55.90%
# space-complexity O(N) 93.05%
# language python
# difficulty hard
# date 20240601