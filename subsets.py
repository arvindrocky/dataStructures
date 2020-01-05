class Solution:
    def subsets(self, nums):
        subsets_so_far = []
        result = []
        self.create_subsets(nums, 0, subsets_so_far, result)
        return result

    def create_subsets(self, nums, index, subsets_so_far, result):
        if len(nums) == index:
            print(subsets_so_far)
            result.append(subsets_so_far.copy())
            return
        else:
            subsets_so_far.append(nums[index])
            self.create_subsets(nums, index + 1, subsets_so_far, result)
            subsets_so_far.pop()
            self.create_subsets(nums, index + 1, subsets_so_far, result)


a = Solution()
#print(a.subsets([1,2,3]))
a.subsets([1,2,3])
