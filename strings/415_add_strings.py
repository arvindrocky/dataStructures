class Solution:
    def __init__(self):
        pass

    def add_two_strings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = ''
        reminder: int = 0
        # while i >= 0 and j >= 0:
        #     temp = int(num1[i]) + int(num2[j]) + reminder
        #     if temp > 9:
        #         temp = temp % 10
        #         reminder = 1
        #     else:
        #         reminder = 0
        #     res = str(temp) + res
        #     i -= 1
        #     j -= 1
        # while i >= 0:
        #     temp = int(num1[i]) + reminder
        #     if temp > 9:
        #         temp = temp % 10
        #         reminder = 1
        #     else:
        #         reminder = 0
        #     res = str(temp) + res
        #     i -= 1
        # while j >= 0:
        #     temp = int(num2[j]) + reminder
        #     if temp > 9:
        #         temp = temp % 10
        #         reminder = 1
        #     else:
        #         reminder = 0
        #     res = str(temp) + res
        #     j -= 1
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            temp = a + b + reminder
            if temp > 9:
                temp = temp % 10
                reminder = 1
            else:
                reminder = 0
            res = str(temp) + res
            i -= 1
            j -= 1
        if reminder > 0:
            res = str(reminder) + res
        return res


sol = Solution()
print(sol.add_two_strings("9989", "99"))
