# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int, left_child: 'TreeNode' = None, right_child: 'TreeNode' = None):
        self.val = x
        self.left = left_child
        self.right = right_child


class Solution:
    def merge_trees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        t1.left = self.merge_trees(t1.left, t2.left)
        t1.right = self.merge_trees(t1.right, t2.right)
        t1.val = t1.val + t2.val
        return t1

    def print_in_order_of_tree(self, node: TreeNode) -> None:
        # left, root, right
        if not node:
            return
        self.print_in_order_of_tree(node.left)
        print(node.val)
        self.print_in_order_of_tree(node.right)


a = Solution()
tree1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
tree2 = TreeNode(5, TreeNode(6, TreeNode(7), TreeNode(8)), TreeNode(3, TreeNode(4, TreeNode(9))))
merged_tree = a.merge_trees(tree1, tree2)
print(a.print_in_order_of_tree(merged_tree))
