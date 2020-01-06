from typing import List


class Solution:
    def __init__(self):
        pass

    def count_number_of_ways(self, steps: List[int], total_number_of_stairs: int) -> int:
        return self.count_number_of_ways_helper(steps, total_number_of_stairs, total_number_of_stairs)

    def count_number_of_ways_helper(self, steps: List[int], total_number_of_stairs, pending_stairs: int) -> int:
        if pending_stairs == 0:
            return 1
        if pending_stairs < 0:
            return 0
        result = 0
        for i in range(len(steps)):
            result += self.count_number_of_ways_helper(steps, total_number_of_stairs, pending_stairs - steps[i])
        return result


a = Solution()
print(a.count_number_of_ways([1, 2, 3], 3))
