class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root.left, root.right)

    def mirror(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return (self.mirror(left.left, right.right) and
                self.mirror(left.right, right.left))