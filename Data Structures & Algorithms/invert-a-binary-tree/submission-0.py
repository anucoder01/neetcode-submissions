class Solution:
    def invertTree(self, root):

        if root == None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root