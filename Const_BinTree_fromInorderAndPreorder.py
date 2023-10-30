class Solution:
    p = []
    def subtree(self,left,right):
        root = TreeNode(self.p.pop(0)) #determining root 

        if len(left) > 1 :            #dividing left subtree further
            r = self.p[0]
            pos = left.index(r)
            l = left[:pos]
            r = left[pos+1:]
            root.left = self.subtree(l,r)
        elif len(left) == 1:
            self.p.remove(left[0])
            root.left = TreeNode(left[0])

        if len(right) > 1 :            #dividing right subtree further
            r = self.p[0]
            pos = right.index(r)
            l = right[:pos]
            r = right[pos+1:]
            root.right = self.subtree(l,r)   
        elif len(right) == 1:
            self.p.remove(right[0])
            root.right = TreeNode(right[0]) 

        return root                     #returning the subtree

    def buildTree(self, p: List[int], i: List[int]) -> Optional[TreeNode]:

        self.p = p
        root = self.p[0]
        pos = i.index(root)
        left = i[:pos]
        right = i[pos+1:]

        return self.subtree(left,right)
        
 