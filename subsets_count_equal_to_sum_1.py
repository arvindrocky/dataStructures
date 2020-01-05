from typing import List


class Solution:
    def __init__(self):
        self.input_list = []
        self.target_sum = 0

    def count_subsets(self, input_list: List[int], target_sum: int) -> int:
        self.input_list = input_list
        self.target_sum = target_sum
        return self.count_subsets_helper(0, self.target_sum)

    def count_subsets_helper(self, counter: int, current_sum: int) -> int:
        if current_sum == 0:
            return 1
        elif counter == len(self.input_list):
            return 0
        elif current_sum < 0:
            return 0
        return self.count_subsets_helper(counter + 1, current_sum) + self.count_subsets_helper(counter + 1,
                                                                                               current_sum -
                                                                                               self.input_list[counter])


sol = Solution()
print(sol.count_subsets([10, 20, 30, 15, 5], 30))
