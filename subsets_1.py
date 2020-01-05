from typing import List


class Solution:
    def __init__(self):
        pass

    def print_subsets(self, input_list: List[int]) -> List[List[int]]:
        res = list()
        subsets_so_far = list()
        res.append(self.print_subsets_helper(input_list, 0, subsets_so_far))
        return res

    def print_subsets_helper(self, input_list: List[int], counter: int, subsets_so_far: List[int]) -> List[List[int]]:
        if counter == len(input_list):
            return subsets_so_far
        a = self.print_subsets_helper(input_list, counter + 1, subsets_so_far)
        d = subsets_so_far.copy()
        d.append(input_list[counter])
        b = self.print_subsets_helper(input_list, counter + 1, d)
        result = list()
        result.append(a)
        result.append(b)
        return result


sol = Solution()
print(sol.print_subsets([10, 20, 30]))