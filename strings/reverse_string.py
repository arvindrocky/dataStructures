class Solution:
    def __init__(self):
        pass

    def reverse_string(self, input_str:str) -> str:
        if not input_str:
            return input_str
        left = 0
        right = len(input_str) - 1
        while left < right:
            input_str = self.str_swap(input_str, left, right)
            left += 1
            right -= 1
        return input_str

    def str_swap(self, s, i, j) -> str:
        # s[i], s[j] = s[j], s[i]
        temp = list(s)
        temp[i], temp[j] = temp[j], temp[i]
        return "".join(temp)


sol = Solution()
print(sol.reverse_string("string"))
