#leetcode-145
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def postorderTraversal(root):
    result = []

    def traverse(node):
        if not node:
            return
        # for child in node.children:
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)

    traverse(root)
    return result
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(postorderTraversal(root))  # Output: [3, 2, 1]