class Solution:
    
    def buildTreeHelper(self, preorder, inorder):
        
        if not preorder or not inorder:
            return 
        
        rootElement = preorder.popleft() #constant
        
        ix = inorder.index(rootElement) #n 
        node = TreeNode(rootElement) 
        
        node.left = self.buildTreeHelper(preorder, inorder[:ix])
        node.right = self.buildTreeHelper(preorder, inorder[ix+1:])
        
        return node
            
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildTreeHelper(collections.deque(preorder), inorder)
    