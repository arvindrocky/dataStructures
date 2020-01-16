from typing import List

class Node:
    def __init__(self, value, left_child: 'Node' = None, right_child: 'Node' = None):
        self.value = value
        self.left_node = left_child
        self.right_node = right_child


class Solution:
    def find_path_where_sum_is_k(self, node: Node, k: int, result: List = []):
        if not node:
            return
        temp_result = result.copy()
        temp_result.append(node.value)
        if node.value == k and not node.left_node and not node.right_node:
            print("Path: {}".format(temp_result))
            return
        if node.value > k:  # no need to traverse further
            return
        self.find_path_where_sum_is_k(node.left_node, k - node.value, temp_result)
        self.find_path_where_sum_is_k(node.right_node, k - node.value, temp_result)


sample_tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6)))
target_sum = 2
a = Solution()
a.find_path_where_sum_is_k(sample_tree, target_sum)
