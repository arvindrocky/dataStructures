class Solution:
    def print_subsets(self, input, index=0):
        if index >= len(input):
            print(input)
        else:
            self.print_subsets(input, index + 1)
            input_copy = input.copy()
            del input_copy[index]
            self.print_subsets(input_copy, index)


sol = Solution()
sol.print_subsets([1,2,3,4])
