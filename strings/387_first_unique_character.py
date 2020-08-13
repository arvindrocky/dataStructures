from collections import Counter

class Solution(object):
    def __init__(self):
        pass

    def get_index_of_first_unique_character(self, input_str: str) -> int:
        unique_characters = {}
        count_characters = list()
        for i, c in enumerate(input_str):
            if c not in unique_characters:
                unique_characters[c] = i
                count_characters.append(1)
            else:
                char_index = unique_characters[c]
                count = count_characters[char_index]
                count_characters[char_index] += 1
                count_characters.append(count + 1)
        i = 0
        while i < len(count_characters):
            if count_characters[i] == 1:
                return i
            i += 1
        return -1


sol = Solution()
print(sol.get_index_of_first_unique_character("leetcode"))
print(sol.get_index_of_first_unique_character("loveleetcode"))
print(sol.get_index_of_first_unique_character("aaa"))
c = Counter("leetcode")
print(c)