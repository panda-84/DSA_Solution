class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

max_sum = float('-inf')

def maxPathSum(root):
    global max_sum
    if root is None:
        return 0

    left = max(0, maxPathSum(root.left))
    right = max(0, maxPathSum(root.right))

    max_sum = max(max_sum, root.val + left + right)

    return root.val + max(left, right)


# Example
root = TreeNode(10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

maxPathSum(root)
print(max_sum) 