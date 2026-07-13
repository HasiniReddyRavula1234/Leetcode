# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        if root is None:
            return []
        q = collections.deque([root])
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                n = q.popleft()
                if n:
                    level.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if level:
                lst.append(level)
        return lst[::-1]
        
