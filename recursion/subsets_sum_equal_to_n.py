class Solution:
    def subsets(self, nums, target):
        subsets_so_far = []
        result = []
        self.create_subsets(nums, 0, subsets_so_far, result, target)
        return result

    def create_subsets(self, nums, index, subsets_so_far, result, target):
        if len(nums) == index:
            if sum(subsets_so_far) == target:
                result.append(subsets_so_far.copy())
        else:
            subsets_so_far.append(nums[index])
            self.create_subsets(nums, index + 1, subsets_so_far, result, target)
            subsets_so_far.pop()
            self.create_subsets(nums, index + 1, subsets_so_far, result, target)


a = Solution()
print(a.subsets([1,2,3,5], 6))
