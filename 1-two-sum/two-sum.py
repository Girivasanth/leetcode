class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n):
            t=target-nums[i]
            print(t)
            if t in nums and nums.index(t)!=i:
                return nums.index(t),i
            else:
                t=0
        