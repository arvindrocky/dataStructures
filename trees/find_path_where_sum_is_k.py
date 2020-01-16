from typing import List

class Node:
    def __init__(self, value, left_child: 'Node' = None, right_child: 'Node' = None):
        self.value = value
        self.left_node = left_child
        self.right_node = right_child


class Solution:
    def find_path_where_sum_is_k(self, node: Node, k: int, result: List = []):
        if not node:
            return False
        temp_result = result.copy()
        temp_result.append(node.value)
        if node.value == k and not node.left_node and not node.right_node:
            print("Path: {}".format(temp_result))
            return True
        if node.value > k:  # no need to traverse further
            return False
        return self.find_path_where_sum_is_k(node.left_node, k - node.value, temp_result) or \
               self.find_path_where_sum_is_k(node.right_node, k - node.value, temp_result)

    def find_all_paths_where_sum_is_k(self, node: Node, k: int, result: List = []):
        if not node:
            return
        temp_result = result.copy()
        temp_result.append(node.value)
        if node.value == k and not node.left_node and not node.right_node:
            print("Path: {}".format(temp_result))
            return
        if node.value > k:
            return
        self.find_all_paths_where_sum_is_k(node.left_node, k - node.value, temp_result)
        self.find_all_paths_where_sum_is_k(node.right_node, k - node.value, temp_result)


sample_tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(4), Node(6)))
target_sum = 8
sol = Solution()
print("Finding the first path whose sum is equal to {}".format(target_sum))
print(sol.find_path_where_sum_is_k(sample_tree, target_sum))

print("Finding all paths whose sum is equal to {}".format(target_sum))
sol.find_all_paths_where_sum_is_k(sample_tree, target_sum)
