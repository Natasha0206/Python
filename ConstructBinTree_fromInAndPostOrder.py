
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return self.construct(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, dic)

    def construct(self, ino, in_start, in_end, post, post_start, post_end, dic) -> TreeNode:
        if in_start > in_end or post_start > post_end:
            return None
        
        root = TreeNode(post[post_end])
        ele_left = dic[root.val] - in_start

        root.left = self.construct(ino, in_start, dic[root.val] - 1, post, post_start, post_start + ele_left - 1, dic)
        root.right = self.construct(ino, dic[root.val] + 1, in_end, post, post_start + ele_left, post_end - 1, dic)

        return root