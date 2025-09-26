# 124. Binary Tree Maximum Path Sum
# hard problem 
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# Exaple 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


# VERY tricky but easy 

from typing import Optional,TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val] #THis is just a global variable same as self.res so That 
                        #It can be accessed inside the function thats all 
        def dfs(root):
            if not root:
                return 0
            leftMax=dfs(root.left)
            rightMax=dfs(root.right)
            leftMax=max(leftMax,0)
            rightMax=max(rightMax,0)

            # Combine EVeruthing to store in res that is root and left right 
            # No SPLIT Take EVERYTHING
            res[0]=max(res[0],root.val+leftMax+rightMax)

            # Dont combine everuthing there is a choice Root and left OR root and right 
            return root.val+ max(leftMax,rightMax)
        dfs(root)
        return res[0]