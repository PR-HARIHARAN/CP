#LC problem link: https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []

        def backtrack(node,sol):
            if node is None:
                return
            if not node.left and not node.right:
                sol+=str(node.val)
                res.append(sol)
                return
            
            sol += str(node.val)+'->'
            if node.left:
                backtrack(node.left,sol)
            if node.right:
                backtrack(node.right,sol)
        backtrack(root,"")
        
        return res
