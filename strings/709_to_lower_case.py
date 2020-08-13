class Solution:
    def to_lower_case(self, str: str) -> str:
        output = ''
        for c in str:
            output += chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c
        return output


sol = Solution()
print(sol.to_lower_case('ABCD'))
print(sol.to_lower_case(''))
print(sol.to_lower_case('AbcD'))
print(sol.to_lower_case('AbcD123Z'))
