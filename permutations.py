class Solution:
    def permute(self, nums):
        self.result = []
        self.permute_list(nums, 0)

    def permute_list(self, a, i):
        if i == len(a) - 1:
            # print(a)
            self.result.append(a)
        else:
            for j in range(i, len(a)):
                #print("i: {} and j: {}".format(i, j))
                a = self.swap_elements(a, i, j)
                self.permute_list(a, i + 1)
                a = self.swap_elements(a, i, j)
                #return b

    def swap_elements(self, a, i, j):
        a[i], a[j] = a[j], a[i]
        return a


a = Solution()
a.permute([10,20,30])
print(a.result)