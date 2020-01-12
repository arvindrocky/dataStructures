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
            return len(regex) - i == regex[i:].count("*")
        if regex[i] == input_str[j]:
            return self.is_matching_regex_helper(regex, input_str, i + 1, j + 1)
        if regex[i] == "*":
            for x in range(j, len(input_str) + 1):
                is_matching = is_matching or self.is_matching_regex_helper(regex, input_str, i + 1, x)
        return is_matching


a = Solution()
print(True if a.is_matching_regex("a", "a") else False)
print(True if a.is_matching_regex("ab", "ab") else False)
print(False if a.is_matching_regex("a", "ab") else True)
print(False if a.is_matching_regex("ab", "a") else True)
print(True if a.is_matching_regex("a*", "a") else False)
print(True if a.is_matching_regex("a**", "a") else False)
print(True if a.is_matching_regex("a***", "a") else False)
print(False if a.is_matching_regex("a*b", "a") else True)
print(False if a.is_matching_regex("a", "ab") else True)
print(True if a.is_matching_regex("a*", "ab") else False)
print(True if a.is_matching_regex("a*", "abc") else False)
print(True if a.is_matching_regex("a*b", "ab") else False)
print(True if a.is_matching_regex("a*b", "acb") else False)
print(True if a.is_matching_regex("a*b", "abdb") else False)
print(False if a.is_matching_regex("a*b", "ac") else True)
print(True if a.is_matching_regex("ab*c*d", "abccaabd") else False)
