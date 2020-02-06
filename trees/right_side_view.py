import queue

from display_tree import DisplayTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int, left_child: 'TreeNode' = None, right_child: 'TreeNode' = None):
        self.val = x
        self.left = left_child
        self.right = right_child


class Solution:
    def print_right_side_view(self, root: TreeNode) -> None:
        current_level: int = 1
        printed_level: int = 0
        right_side_queue: queue = queue.Queue(0)
        right_side_queue.put(root)
        right_side_queue.put(current_level)
        while not right_side_queue.empty():
            current_node: TreeNode = right_side_queue.get()
            current_level = right_side_queue.get()
            if current_node:
                if current_level != printed_level:
                    print(current_node.val)
                    printed_level = printed_level + 1
                right_side_queue.put(current_node.right)
                right_side_queue.put(current_level + 1)
                right_side_queue.put(current_node.left)
                right_side_queue.put(current_level + 1)

    def print_right_side_view_1(self, node1: TreeNode, node2: TreeNode) -> TreeNode:
        if not node1:
            return node2
        if not node2:
            return node1
        node = TreeNode(node2.val)
        node.left = self.print_right_side_view_1(node1.left, node1.right)
        node.right = self.print_right_side_view_1(node2.left, node2.right)
        return node


tree1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
tree2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(10))), TreeNode(3, TreeNode(6), TreeNode(7)))
tree3 = TreeNode(1, TreeNode(2, None, TreeNode(3, TreeNode(4, None, TreeNode(5, TreeNode(6), TreeNode(7))))))

sol:Solution = Solution()

print("Printing Full Tree1:")
DisplayTree.display(tree2)

print("Printing Right Side View of Tree1:")
sol.print_right_side_view(tree2)

print("Printing Right Side View-1 of Tree1:")
DisplayTree.display(sol.print_right_side_view_1(tree2.left, tree2.right))
