class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if root == None or root.val == p.val or root.val == q.val:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root