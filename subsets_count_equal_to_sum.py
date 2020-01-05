from typing import List


class Solution:
    def __init__(self):
        self.input_list = []
        self.target_sum = 0

    def count_subsets(self, input_list: List[int], target_sum: int) -> int:
        self.input_list = input_list
        self.target_sum = target_sum
        return self.count_subsets_helper(0, 0)

    def count_subsets_helper(self, current_sum: int, counter: int) -> int:
        if current_sum == self.target_sum:
            return 1
        if counter == len(self.input_list):
            return 0
        if current_sum > self.target_sum:
            return 0
        return self.count_subsets_helper(current_sum, counter + 1) + \
               self.count_subsets_helper(current_sum + self.input_list[counter], counter + 1)


sol = Solution()
print(sol.count_subsets([10, 20, 30, 15, 5], 30))
