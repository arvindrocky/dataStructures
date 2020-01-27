class Solution:
    def __init__(self):
        pass

    def is_palindrom(self, input_str: str) -> bool:
        if not input_str:
            return True
        left = 0
        right = len(input_str) - 1
        while left < right and input_str[left] == input_str[right]:
            left += 1
            right -= 1
        return left >= right


sol = Solution()
print(sol.is_palindrom("tacocat"))
print(sol.is_palindrom("racecar"))
print(sol.is_palindrom("abccba"))
print(sol.is_palindrom("aa"))
print(sol.is_palindrom(""))
print(sol.is_palindrom(None))
print(sol.is_palindrom("arvind"))
print(sol.is_palindrom("avinash"))
