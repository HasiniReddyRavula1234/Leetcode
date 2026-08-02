# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def postorder(root):
            if root is None:
                return []
            postorder(root.left)
            postorder(root.right)
            lst.append(root.val)
            return lst
        return postorder(root)






















    #     lst = []
    #     self.postorder(root, lst)
    #     return lst
    # def postorder(self, root, lst):
    #     if root is None:
    #         return 
    #     self.postorder(root.left, lst)
    #     self.postorder(root.right, lst)
    #     lst.append(root.val)