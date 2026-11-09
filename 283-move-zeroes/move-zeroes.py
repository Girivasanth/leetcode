class Solution(object):
    def moveZeroes(self, nums):
        l = len(nums)
        for i in range(l-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
        while len(nums) < l:
            nums.append(0)