#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution:
    def lcaHelper(self, node, a, b):
        
        if not node:
            return 
        
        if node == a:
            return a
        
        if node == b:
            return b
        
        left = self.lcaHelper(node.left, a,b)
        right = self.lcaHelper(node.right, a,b)
        
        if left and right: 
            return node
        
        if left and not right: 
            return left
        
        if right and not left: 
            return right
        
        if not left and not right: 
            return 
        
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lcaHelper(root,p,q)