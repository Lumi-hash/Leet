class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, x in enumerate(nums):
            partner = target - x
            if partner in lookup:
                return [lookup[partner], i]
            lookup[x] = i

#--- testing ---
s = Solution()   

print(s.twoSum([2, 7, 11, 15], 9))   # expect [0, 1]
print(s.twoSum([3, 2, 4], 6))        # expect [1, 2]
print(s.twoSum([3, 3], 6))           # expect [0, 1]
