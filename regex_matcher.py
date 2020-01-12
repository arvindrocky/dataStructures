from typing import List


class Solution:
    def __init__(self):
        pass

    def is_matching_regex(self, regex: str, input_str: str) -> bool:
        return self.is_matching_regex_helper(regex, input_str, 0, 0)

    def is_matching_regex_helper(self, regex: str, input_str: str, i: int, j: int) -> bool:
        is_matching = False
        if i == len(regex):
            return j == len(input_str)
        if j == len(input_str):
            if i == len(regex)-1 and regex[i] == "*":
                return True
            else:
                return False
        if regex[i] == input_str[j]:
            return self.is_matching_regex_helper(regex, input_str, i+1, j+1)
        if regex[i] == "*":
            for x in range(j, len(input_str)+1):
                is_matching = is_matching or self.is_matching_regex_helper(regex, input_str, i+1, x)
        return is_matching


a = Solution()
print(True == a.is_matching_regex("a", "a"))
print(True == a.is_matching_regex("ab", "ab"))
print(False == a.is_matching_regex("a", "ab"))
print(False == a.is_matching_regex("ab", "a"))
print(True == a.is_matching_regex("a*", "a"))
print(False == a.is_matching_regex("a", "ab"))
print(True == a.is_matching_regex("a*", "abc"))
print(True == a.is_matching_regex("a*b", "ab"))
print(True == a.is_matching_regex("a*b", "acb"))
print(True == a.is_matching_regex("a*b", "abdb"))
print(False == a.is_matching_regex("a*b", "ac"))

