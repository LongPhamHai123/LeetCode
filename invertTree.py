#leetcode - 226
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invertTree(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)
    return root