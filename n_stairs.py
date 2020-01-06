from typing import List


class Solution:
    def __init__(self):
        pass

    def count_number_of_ways(self, steps: List[int], total_number_of_stairs: int) -> int:
        return self.count_number_of_ways_helper(steps, total_number_of_stairs, 0)

    def count_number_of_ways_helper(self, steps: List[int], total_number_of_stairs: int,
                                    number_of_stairs_climbed: int) -> int:
        if number_of_stairs_climbed == total_number_of_stairs:
            return 1
        if number_of_stairs_climbed > total_number_of_stairs:
            return 0
        result = 0
        for i in range(len(steps)):
            result += self.count_number_of_ways_helper(steps, total_number_of_stairs, number_of_stairs_climbed +
                                                       steps[i])
        return result


sol = Solution()
print(sol.count_number_of_ways([1, 2, 3], 3))
