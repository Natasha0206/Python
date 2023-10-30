
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.maximum=1e8
        if root==None:
            return 0
        def topToBottom(node, depth):
            if not node.left and not node.right:
                self.maximum=min(self.maximum, depth+1)
            if node.left:
                topToBottom(node.left, depth+1)
            if node.right:
                topToBottom(node.right, depth+1)
        topToBottom(root, 0)
        return self.maximum  